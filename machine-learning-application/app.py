from flask import Flask
from pipelines import real_time_predict_pipeline, real_time_train_pipeline
from utils import auxiliary_functions as af

app = Flask(__name__)
list_cryptos_to_train = list(af.get_all_available_cryptos()['db_crypto_name'].values)
@app.route('/')
def nothing():
    return 'Sucess !'

@app.route('/train-1')
def train_model():
    real_time_train_pipeline.RealTimeTrain(list_cryptos_to_train=list_cryptos_to_train[0:5]).train_pipeline()
    return "Train 1 sucessfull !"

@app.route('/train-2')
def train_model_2():
    real_time_train_pipeline.RealTimeTrain(list_cryptos_to_train=list_cryptos_to_train[5:10]).train_pipeline()
    return "Train 2 sucessfull !"

@app.route('/train-3')
def train_model_3():
    real_time_train_pipeline.RealTimeTrain(list_cryptos_to_train=list_cryptos_to_train[10:15]).train_pipeline()
    return "Train 3 sucessfull !"

@app.route('/train-4')
def train_model_4():
    real_time_train_pipeline.RealTimeTrain(list_cryptos_to_train=list_cryptos_to_train[15:20]).train_pipeline()
    return "Train 4 sucessfull !"


@app.route('/predict')
def predict():
    real_time_predict_pipeline.RealTimePredict().predict_pipeline()
    return "Predict sucessfull !"

if __name__ == "__main__":
	app.run(host='0.0.0.0')