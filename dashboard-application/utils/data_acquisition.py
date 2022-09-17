from queue import Empty
import psycopg2
from datetime import datetime, timedelta
import json
import pandas as pd
import math
class DataAcquisition():
    def __init__(self):
        self.output_data = pd.DataFrame()


    def create_min_column(self):
        price = []
        for index,row in self.output_data.iterrows():
            price.append(row['price'])

        min_column = []
        for i,value in enumerate(price):
            if (i==0):
                menor = value
                min_column.append(menor)
            else:
                if i%13==0:
                    menor = math.inf
                if value < menor:
                    menor = value
                    min_column.append(menor)
                else:
                    min_column.append(menor)
        self.output_data['min_1h'] = min_column
        

    def create_max_column(self):
        price = []
        for index,row in self.output_data.iterrows():
            price.append(row['price'])

        max_column = []
        for i,value in enumerate(price):
            if (i==0):
                maior = value
                max_column.append(maior)
            else:
                if i%13==0:
                    maior = -math.inf
                if value > maior:
                    maior = value
                    max_column.append(maior)
                else:
                    max_column.append(maior)
        self.output_data['max_1h'] = max_column
        

    def get_data(self,crypto_name='bitcoin',
                start_date = (datetime.now()-timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S'),
                end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
        
        
        config_data = json.load(open('../configs.json'))
        conn = psycopg2.connect(
            host = config_data['host'], 
            database = config_data['database'],
            user = config_data['user'],
            password = config_data['password']
            )

        query = f"SELECT * FROM {crypto_name} WHERE date BETWEEN '{start_date}' and '{end_date}'"
        self.output_data = pd.read_sql(query,conn)

    def data_acquisition_pipeline(self,crypto_name='bitcoin',
                start_date = (datetime.now()-timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S'),
                end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
        self.get_data(crypto_name,start_date,end_date)
        self.create_max_column()
        self.create_min_column()
        return self.output_data