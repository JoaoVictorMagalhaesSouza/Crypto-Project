
import web_scraping, insert_data, data_verification
import time
import schedule
print(f'STARTING THE DATABASE POPULATION...')

def realiza_scrapper():
    names,symbols,price,market_cap,vol = web_scraping.Scrapper().get_available_cryptos()
    alter_names = []
    for name in names:
        alter_names.append(name.replace(' ','').replace('-','').replace('1','One').lower())
        
    verify = data_verification.DatabaseVerification(alter_names).get_all_existing_table_names()
    data = insert_data.InsertData(price,market_cap,vol,alter_names)
    data.insert_data_into_database()

schedule.every(1).minutes.do(realiza_scrapper)
while True:
    schedule.run_pending()
    time.sleep(1)