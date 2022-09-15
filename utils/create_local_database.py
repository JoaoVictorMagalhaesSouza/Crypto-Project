#%%
import psycopg2
#%% Creating the conetion

'''
    Change here !!!
'''
conn = psycopg2.connect(
    host = 'host',
    database = 'database',
    user = 'user',
    password = 'password'
)
cursor = conn.cursor()
#%% Creating the tables
import web_scraping

names,symbols,price,market_cap,vol = web_scraping.Scrapper().get_available_cryptos()
for name in names:
    name = name.replace(' ','').replace('-','').replace('1','One')
    script = f"""CREATE TABLE {name} (Date TIMESTAMP NOT NULL, Price FLOAT(32), MarketCap FLOAT(32), Volume FLOAT(32) );"""
    cursor.execute(script)
cursor.close()
conn.commit()
# %%
