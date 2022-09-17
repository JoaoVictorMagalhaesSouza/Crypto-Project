import pandas as pd
from copy import deepcopy
import math

class DataPreparation():
    def __init__(self, initial_data: pd.DataFrame):
        self.output_data = deepcopy(initial_data)

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
    
    def create_target_column(self):
        #5min
        self.output_data['future_price'] = self.output_data['price'].shift(-1)
        
    
    def data_preparation_pipeline_realtime(self):
        self.create_max_column()
        self.create_min_column()
        self.create_target_column()
        data_for_predict = self.output_data.tail(1)
        data_for_train = self.output_data[:-1]
        return data_for_train, data_for_predict



