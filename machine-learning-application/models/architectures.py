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
            #TODO:
            # Call param optimization here
            self.model = XGBRegressor(n_estimators=50, max_depth=4, eval_metric = 'mae')
    
    def fit(self):
        self.model.fit(self.X_train,self.y_train)
    
    def predict(self):
        return self.model.predict(self.X_test)

