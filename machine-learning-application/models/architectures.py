from xgboost import XGBRegressor
import tensorflow as tf

class XGBModel():
    def __init__(self):

        self.model = None

    def init_model(self, params = None):
        
        if params != None:
            self.model = XGBRegressor(**params)
        else:
            #TODO:
            # Call param optimization here
            self.model = XGBRegressor(n_estimators=50, max_depth=4, eval_metric = 'mae')
    
    def fit(self, X_train, y_train):
        self.model.fit(X_train,y_train)
    
    def predict(self, X_test):
        return self.model.predict(X_test)

