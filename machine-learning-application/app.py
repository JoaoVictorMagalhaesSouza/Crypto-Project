from flask import Flask
from pipelines import real_time_predict_pipeline, real_time_train_pipeline

app = Flask(__name__)

@app.route('/train')
def train_model():
    real_time_train_pipeline.RealTimeTrain().train_pipeline()
    return "Train sucessfull !"

@app.route('/predict')
def predict():
    real_time_predict_pipeline.RealTimePredict().predict_pipeline()
    return "Predict sucessfull !"

if __name__ == "__main__":
	app.run(host='0.0.0.0')