
import sys
import joblib
sys.path.append('../')

from utils import data_acquisition as da
from utils import data_preparation as dp
from utils import split_data as sd
from utils import auxiliary_functions as af
from models import architectures as arch

class RealTimeTrain():
    def __init__(self, list_cryptos_to_train = af.get_all_available_cryptos()['db_crypto_name'].values):
        self.to_train = list_cryptos_to_train
    
    def train_pipeline(self):
        for crypto in self.to_train:
            print(f"Training {crypto} model...")
            data = da.DataAcquisition().data_acquisition_pipeline(crypto_name=crypto)
            prepared_data = dp.DataPreparation(data).data_preparation_pipeline_realtime()
            X_train, y_train, train_dates = sd.SplitData(prepared_data).split_real_time()

            #Here we go to apply optuna to decide best model for wich crypto...
            model = arch.XGBModel()
            model.init_model()
            model.fit(X_train, y_train)
            ###
            
            filename = f"../saved_models/{crypto}_model.joblib"
            joblib.dump(model,filename)
            print(" => OK")
