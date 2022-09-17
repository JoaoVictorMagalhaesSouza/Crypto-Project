#%%
import sys
from sklearn.metrics import mean_absolute_error, mean_squared_error
sys.path.append('../')

from utils import data_acquisition as da
from utils import data_preparation as dp
from utils import split_data as sd
from models import architectures as arch
#%%
data = da.DataAcquisition().data_acquisition_pipeline()
data = dp.DataPreparation(data).data_preparation_pipeline()
# %%
X_train, y_train, X_test, y_test, train_dates, test_dates = sd.SplitData(data).split_train_test()
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