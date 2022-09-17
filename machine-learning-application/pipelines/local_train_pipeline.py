#%%
import sys
from sklearn.metrics import mean_absolute_error, mean_squared_error
sys.path.append('../')

from utils import data_acquisition as da
from utils import data_preparation as dp
from utils import split_data as sd
from utils import auxiliary_functions as af
from models import architectures as arch
#%%
all_available_cryptos = af.get_all_available_cryptos()['db_crypto_name'].values
#%%
data = da.DataAcquisition().data_acquisition_pipeline()
data_for_train, data_for_predict = dp.DataPreparation(data).data_preparation_pipeline_local()
#%%
X_train, y_train, X_test, y_test, train_dates, test_dates = sd.SplitData(data_for_train).split_train_test()
#%%
model = arch.XGBModel(X_train, X_test, y_train, y_test)
model.init_model()
model.fit()
result = model.predict()
#%% Performance
print(f"MAE: {mean_absolute_error(result,y_test)}")
print(f'MSE: {mean_squared_error(result,y_test)}')
print(f"RMSE: {mean_squared_error(result,y_test,squared=False)}")
#%%