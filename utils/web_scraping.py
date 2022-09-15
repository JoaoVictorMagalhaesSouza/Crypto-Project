from bs4 import BeautifulSoup
import requests
from locale import setlocale, LC_NUMERIC
setlocale(LC_NUMERIC, '')

class Scrapper():
    def __init__(self):
        self.html = requests.get('https://www.investing.com/crypto/currencies').content
        self.soup = BeautifulSoup(self.html, 'html.parser')
    
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

        return all_available_cryptos_names, all_available_cryptos_symbols, all_available_cryptos_price, all_available_cryptos_market_cap, all_available_cryptos_vol