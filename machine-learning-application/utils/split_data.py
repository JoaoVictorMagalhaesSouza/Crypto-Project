import pandas as pd
from copy import deepcopy
class SplitData():
    def __init__(self, data: pd.DataFrame):
        self.data = deepcopy(data)
    

    def split_train_test(self, train_size=0.8):
        len_dataset = len(self.data)
        
        df_train = self.data.loc[:len_dataset*train_size]
        df_test = self.data.loc[len_dataset*train_size:]
        train_dates = df_train.pop('date')
        test_dates = df_test.pop('date')
        X_train, y_train = df_train.drop(columns={'future_price'}), df_train['future_price']
        X_test, y_test = df_test.drop(columns={'future_price'}), df_test['future_price']
        
        return X_train, y_train, X_test, y_test, train_dates, test_dates