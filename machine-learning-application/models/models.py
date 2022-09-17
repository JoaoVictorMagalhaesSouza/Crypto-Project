from xgboost import XGBRegressor
import tensorflow as tf

class XGBModel():
    def __init__(self, X_train, X_test, y_train, y_test):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test

        self.model = None

    def init_model(self, params = None):
        
        if params != None:
            self.model = XGBRegressor(**params)
        else:
            pass
            #Call param optimization here

