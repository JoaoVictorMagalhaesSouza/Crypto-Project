# %%
from utils import web_scraping, insert_data

names,symbols,price,market_cap,vol = web_scraping.Scrapper().get_available_cryptos()
alter_names = []
for name in names:
    alter_names.append(name.replace(' ','').replace('-','').replace('1','One'))
#%% Test
data = insert_data.InsertData(price,market_cap,vol,alter_names)
#%%
data.insert_data_into_database()

# %%
import time

while True:
    timeBegin = time.time()

    print("Hora de peggar")

    timeEnd = time.time()
    timeElapsed = timeEnd - timeBegin
    time.sleep(60-timeElapsed)
# %%
