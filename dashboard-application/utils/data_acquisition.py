import psycopg2
from datetime import datetime, timedelta

def get_data(crypto_name, start_date = (datetime.now()-timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S'), end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
    conn = psycopg2.connect(
        host = 'confidential',
        database = 'postgres',
        user = 'postgres',
        password = 'confidential'
        )
    cursor = conn.cursor()

    query = f"SELECT * FROM {crypto_name} WHERE date BETWEEN '{start_date}' and '{end_date}'"
