from queue import Empty
import psycopg2
from datetime import datetime, timedelta
import json
import pandas as pd
import math
import sys
sys.path.append('../')

class DataAcquisition():
    def __init__(self):
        self.output_data = pd.DataFrame()


    def get_data(self,crypto_name='bitcoin'):
        
        
        config_data = json.load(open('../configs.json'))
        conn = psycopg2.connect(
            host = config_data['host'], 
            database = config_data['database'],
            user = config_data['user'],
            password = config_data['password']
            )

        query = f"SELECT * FROM {crypto_name}"
        self.output_data = pd.read_sql(query,conn)
    
    def get_data_predict(self,crypto_name='bitcoin'):
        
        
        config_data = json.load(open('configs.json'))
        conn = psycopg2.connect(
            host = config_data['host'], 
            database = config_data['database'],
            user = config_data['user'],
            password = config_data['password']
            )

        query = f"SELECT * FROM {crypto_name} ORDER BY date DESC LIMIT 1;"
        self.output_data = pd.read_sql(query,conn)

    def data_acquisition_pipeline(self,crypto_name='bitcoin'):
        self.get_data(crypto_name)
        return self.output_data
    
    def data_acquisition_pipeline_predict(self,crypto_name='bitcoin'):
        self.get_data_predict(crypto_name)
        return self.output_data