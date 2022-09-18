import psycopg2
from datetime import datetime, timedelta
import json
import pandas as pd
import sys
sys.path.append('../')

def get_all_available_cryptos():
    config_data = json.load(open('configs.json'))
    conn = psycopg2.connect(
        host = config_data['host'], 
        database = config_data['database'],
        user = config_data['user'],
        password = config_data['password']
        )

    query = "SELECT * FROM cryptos"
    data = pd.read_sql(query,conn)
    return data