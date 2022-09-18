import optuna
from copy import deepcopy
import sys
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
class OptimizeModel():

    def __init__(self, X_train, y_train, X_test, y_test):
        self.X_train = deepcopy(X_train)
        self.y_train = deepcopy(y_train)
        self.X_test = deepcopy(X_test)
        self.y_test = deepcopy(y_test)
    

    def objective(self, trial):
        params = {
        'max_depth': trial.suggest_int('max_depth', 2, 12),
        'n_estimators': trial.suggest_int('n_estimators', 10, 500),
        'eval_metric': trial.suggest_categorical('eval_metric', ['mae', 'rmse']),
        'learning_rate': trial.suggest_loguniform('learning_rate', 1e-5, 0.1),
        'subsample': trial.suggest_uniform('subsample', 0.5, 1.0),
        'colsample_bytree': trial.suggest_uniform('colsample_bytree', 0.5, 1.0),
        'min_child_weight': trial.suggest_uniform('min_child_weight',1, 8)
        }

        model = XGBRegressor(**params)
        model.fit(self.X_train, self.y_train)
        result = model.predict(self.X_test)
        rmse = mean_squared_error(result,self.y_test, squared=False)
        return rmse
    
    def optimize_model(self):
        study = optuna.create_study(direction='minimize')
        study.optimize(self.objective,n_trials=300)

        return study.best_params