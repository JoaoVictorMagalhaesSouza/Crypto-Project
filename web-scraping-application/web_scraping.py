from bs4 import BeautifulSoup
import requests
from locale import atof, setlocale, LC_NUMERIC
setlocale(LC_NUMERIC, '')

class Scrapper():
    def __init__(self):
        self.html = requests.get('https://www.investing.com/crypto/currencies').content
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.focus = ['Bitcoin', 'Ethereum', 'Tether', 'Cardano', 'Dogecoin', "Stellar", 'XRP', "Polkadot",
                    'Neo', 'Celsius', "Aave", 'Cosmos', 'Shiba Inu', 'TRON', 'BNB', 'Polygon', 'Dash',
                    'Tezos', 'Hedera', 'Monero'
                    ]
    
    def get_available_cryptos(self):
        all_html = self.soup.find_all('td')
        all_available_cryptos_symbols = []
        all_available_cryptos_names = []
        all_available_cryptos_price = []
        all_available_cryptos_market_cap = []
        all_available_cryptos_vol = []
        
        for element in all_html:
            if ['left','bold','elp','name','cryptoName','first','js-currency-name'] == element.attrs['class']:
                all_available_cryptos_names.append(element.attrs['title'])
            
            elif ['left', 'noWrap', 'elp', 'symb', 'js-currency-symbol'] == element.attrs['class']:
                all_available_cryptos_symbols.append(element.attrs['title'])
            
            elif ['price', 'js-currency-price'] == element.attrs['class']:
                all_available_cryptos_price.append(float(str(element.text).replace(',','')))
            
            elif ['js-market-cap'] == element.attrs['class']:
                all_available_cryptos_market_cap.append(element.attrs['data-value'])
            
            elif ['js-24h-volume'] == element.attrs['class']:
                all_available_cryptos_vol.append(element.attrs['data-value'])
        
        keep_indexes = []
        for i,crypto in enumerate(all_available_cryptos_names):
            if crypto in self.focus:
                keep_indexes.append(i)
        
        all_available_cryptos_names = [all_available_cryptos_names[i] for i in keep_indexes]
        all_available_cryptos_symbols = [all_available_cryptos_symbols[i] for i in keep_indexes]
        all_available_cryptos_price = [all_available_cryptos_price[i] for i in keep_indexes]
        all_available_cryptos_market_cap = [all_available_cryptos_market_cap[i] for i in keep_indexes]
        all_available_cryptos_vol = [all_available_cryptos_vol[i] for i in keep_indexes]
       
                
        return all_available_cryptos_names, all_available_cryptos_symbols, all_available_cryptos_price, all_available_cryptos_market_cap, all_available_cryptos_vol