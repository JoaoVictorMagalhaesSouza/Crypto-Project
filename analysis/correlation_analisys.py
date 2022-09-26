#%%
import pandas as pd
import json
import psycopg2
#%%
config_data = json.load(open('configs.json'))
conn = psycopg2.connect(
        host = config_data['host'], 
        database = config_data['database'],
        user = config_data['user'],
        password = config_data['password']
        )
cursor = conn.cursor()

query = """SELECT table_name
            FROM information_schema.tables
            WHERE table_schema='public'
            AND table_type='BASE TABLE';
        """
cursor.execute(query)
all_tables = cursor.fetchall()
array_all_tables = []
for table in all_tables:
    array_all_tables.append(table[0])
array_all_tables.remove('models')
array_all_tables.remove('bitcoin')
array_all_tables.remove('cryptos')

#%%
query = f'SELECT * FROM bitcoin'
btc_data = pd.read_sql(query,conn)
corr_data = pd.DataFrame()
corr_data['bitcoin'] = btc_data['price']

for crypto in array_all_tables:
    query = f'SELECT * FROM {crypto}'
    data = pd.read_sql(query,conn)
    corr_data[f'{crypto}'] = data['price']

correlation = corr_data.corr()['bitcoin'].sort_values(ascending=False)
#%%