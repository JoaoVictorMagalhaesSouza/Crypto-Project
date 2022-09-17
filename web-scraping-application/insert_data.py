import psycopg2
from datetime import datetime, timedelta
import json
class InsertData():
    def __init__(self, price, market_cap, volume, alter_names):
        self.price = price
        self.market_cap = market_cap
        self.volume = volume
        self.alter_names = alter_names
        self.config_data = json.load(open('configs.json'))
    
    def insert_data_into_database(self):
        conn = psycopg2.connect(
        host = self.config_data['host'], 
        database = self.config_data['database'],
        user = self.config_data['user'],
        password = self.config_data['password']
        )
        cursor = conn.cursor()
        date = (datetime.now()-timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')
        for position, crypto in enumerate(self.alter_names):
            
            price = self.price[position]
            volume = self.volume[position]
            market_cap = self.market_cap[position]
            script = f"""INSERT INTO {crypto}(date, price, marketcap, volume) 
                    VALUES ('{date}',{price},{market_cap},{volume})
            """
            cursor.execute(script)
        print(f'{date} - Populated successfull!')
        cursor.close()
        conn.commit()

