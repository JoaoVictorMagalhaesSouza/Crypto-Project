from flask import Flask
import requests
import json
import web_scraping, insert_data, data_verification
app = Flask(__name__)

@app.route('/')
def populate():
    print(f'STARTING THE DATABASE POPULATION...')
    names,symbols,price,market_cap,vol = web_scraping.Scrapper().get_available_cryptos()
    alter_names = []
    for name in names:
        alter_names.append(name.replace(' ','').replace('-','').replace('1','One').lower())
        
    verify = data_verification.DatabaseVerification(names, alter_names).get_all_existing_table_names()
    data = insert_data.InsertData(price,market_cap,vol,alter_names)
    data.insert_data_into_database()
    #Predict
    url = json.load(open('configs.json'))['url_predict']
    requests.get(url)
    return 'Sucess!'

if __name__ == "__main__":
	app.run(host='0.0.0.0')
