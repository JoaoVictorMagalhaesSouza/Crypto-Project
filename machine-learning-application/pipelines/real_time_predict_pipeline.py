import sys
import pandas as pd
import psycopg2
import json
import joblib
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings("ignore")
sys.path.append('../')

from utils import data_acquisition as da
from utils import data_preparation as dp
from utils import auxiliary_functions as af

class RealTimePredict():

    def __init__(self, list_cryptos_to_predict = af.get_all_available_cryptos()['db_crypto_name'].values):
        
        self.to_predict = list_cryptos_to_predict

    def save_predictions_into_database(self, crypto, date, predict):
        config_data = json.load(open('configs.json'))
        conn = psycopg2.connect(
            host = config_data['host'], 
            database = config_data['database'],
            user = config_data['user'],
            password = config_data['password']
            )
        cursor = conn.cursor()

        query = f"UPDATE {crypto} SET predicted_value = '{predict}' WHERE (date = '{date}')"
        cursor.execute(query)
        cursor.close()
        conn.commit()
        
    def predict_pipeline(self):
        for crypto in self.to_predict:
            data = da.DataAcquisition().data_acquisition_pipeline_predict(crypto_name=crypto)
            dates = pd.to_datetime(str(data.tail(1)['date'].values[0])) 
            last_date = dates.strftime('%Y-%m-%d %H:%M:%S')
            prepared_data = dp.DataPreparation(data).data_preparation_predict_pipeline_realtime()
            config_data = json.load(open('configs.json'))
            conn = psycopg2.connect(
                host = config_data['host'], 
                database = config_data['database'],
                user = config_data['user'],
                password = config_data['password']
                )
            query = f"SELECT model_name FROM models WHERE crypto = '{crypto}'"
            model_name = pd.read_sql(query,conn).values[0][0]
            path = 'saved_models/'
            model = joblib.load(f'{path}{model_name}')
            predict = model.predict(prepared_data)[0]
            self.save_predictions_into_database(crypto,last_date,predict)

            