
import sys
import joblib
import json
import psycopg2
import pandas as pd
from datetime import datetime, timedelta
sys.path.append('../')

from utils import data_acquisition as da
from utils import data_preparation as dp
from utils import split_data as sd
from utils import auxiliary_functions as af
from models import architectures as arch
from model_param_optimization import optimize_model as om

class RealTimeTrain():
    def __init__(self, list_cryptos_to_train = af.get_all_available_cryptos()['db_crypto_name'].values):
        self.to_train = list_cryptos_to_train
    
    def save_data_into_database(self,crypto, model_name):
        config_data = json.load(open('../configs.json'))
        conn = psycopg2.connect(
            host = config_data['host'], 
            database = config_data['database'],
            user = config_data['user'],
            password = config_data['password']
            )
        cursor = conn.cursor()
        query = f'SELECT * FROM models'
        data = pd.read_sql(query,conn)
        cryptos = data['crypto'].values
        now = (datetime.now()-timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')
        
        if crypto in cryptos:
            query = f"UPDATE models SET last_train = '{now}' WHERE (crypto = '{crypto}')"
            cursor.execute(query)

        else:
            query = f"INSERT INTO models (crypto, model_name, last_train) VALUES ('{crypto}','{model_name}','{now}')"
            cursor.execute(query)
        
        cursor.close()
        conn.commit()

    def train_pipeline(self):
        for crypto in self.to_train:
            print(f"Training {crypto} model...")
            data = da.DataAcquisition().data_acquisition_pipeline(crypto_name=crypto)
            prepared_data = dp.DataPreparation(data).data_preparation_train_pipeline_realtime()
            X_train, y_train, train_dates = sd.SplitData(prepared_data).split_real_time()

            #Here we go to apply optuna to decide best model for wich crypto...
            X_train_splited, y_train_splited, X_test_splited, y_test_splited, train_dates_splited, test_dates_splited = sd.SplitData(prepared_data).split_train_test()
            best_params = om.OptimizeModel(X_train_splited,y_train_splited,X_test_splited,y_test_splited).optimize_model()
            print(X_train)
            model = arch.XGBModel()
            model.init_model(params=best_params)
            model.fit(X_train,y_train)
            model_family = 'xgb'
            ###
            
            filename = f"../saved_models/{crypto}_model_{model_family}.joblib"
            joblib.dump(model,filename)
            self.save_data_into_database(crypto,f'{crypto}_model_{model_family}.joblib')
