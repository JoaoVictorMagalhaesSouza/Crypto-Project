import psycopg2
from datetime import datetime, timedelta
import json
def get_data(crypto_name, start_date = (datetime.now()-timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S'), end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
    config_data = json.load(open('configs.json'))
    conn = psycopg2.connect(
        host = config_data['host'], 
        database = config_data['database'],
        user = config_data['user'],
        password = config_data['password']
        )
    cursor = conn.cursor()

    query = f"SELECT * FROM {crypto_name} WHERE date BETWEEN '{start_date}' and '{end_date}'"
