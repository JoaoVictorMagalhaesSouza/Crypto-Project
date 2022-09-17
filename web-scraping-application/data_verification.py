import psycopg2
from datetime import datetime, timedelta
import json
class DatabaseVerification():
    def __init__(self, names, alter_names):
        self.alter_names = alter_names
        self.original_names = names
        self.config_data = json.load(open('configs.json'))
    

    def get_all_existing_table_names(self):
        conn = psycopg2.connect(
        host = self.config_data['host'], 
        database = self.config_data['database'],
        user = self.config_data['user'],
        password = self.config_data['password']
        )
        cursor = conn.cursor()

        query = """SELECT table_name
                    FROM information_schema.tables
                    WHERE table_schema='public'
                    AND table_type='BASE TABLE';
                """
        cursor.execute(query)
        all_tables = cursor.fetchall()
        cursor.close()
        conn.commit()

        array_all_tables = []
        for table in all_tables:
            array_all_tables.append(table[0])
        
        for crypto in self.alter_names:
            if crypto not in array_all_tables:
                cursor = conn.cursor()
                script = f"""CREATE TABLE {crypto} (Date TIMESTAMP NOT NULL, Price FLOAT(32), MarketCap FLOAT(32), Volume FLOAT(32) );"""
                cursor.execute(script)
        cursor.close()
        conn.commit()

        cursor = conn.cursor()
        query = """SELECT crypto_name FROM cryptos"""
        cursor.execute(query)
        all_cryptos = cursor.fetchall()
        list_original_name_to_insert = []
        list_db_name_to_insert = []
        list_original_name_to_update = []
        list_db_name_to_update = []
        availables = []

        for crypto in all_cryptos:
            availables.append(crypto[0])
        cursor.close()
        conn.commit()

        for i,crypto in enumerate(self.original_names):
            if crypto not in availables:
                list_original_name_to_insert.append(crypto)
                list_db_name_to_insert.append(self.alter_names[i])
            else:
                list_original_name_to_update.append(crypto)
                list_db_name_to_update.append(self.alter_names[i])
                

        cursor = conn.cursor()
        date = (datetime.now()-timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')

        for i,crypto in enumerate(list_original_name_to_insert):
            query = f"INSERT INTO cryptos (crypto_name, db_crypto_name, last_update) VALUES ('{crypto}','{list_db_name_to_insert[i]}','{date}')"
            cursor.execute(query)
        
        cursor.close()
        conn.commit()

        cursor = conn.cursor()
        for i, crypto in enumerate(list_original_name_to_update):
            query  = f"UPDATE cryptos SET last_update = '{date}' WHERE (crypto_name='{crypto}' AND db_crypto_name='{list_db_name_to_update[i]}')"
            cursor.execute(query)
        
        cursor.close()
        conn.commit()





        

