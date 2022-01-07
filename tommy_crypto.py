from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import time




url = requests.get('https://coinmarketcap.com/')
soup = BeautifulSoup(url.content, 'html.parser')

data = soup.find('script', id="__NEXT_DATA__", type="application/json")

coins = {}

#using data.contents[0] to remove script tags
coin_data = json.loads(data.contents[0])
listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']


for i in listings[1:]:
    # print(i['slug'])
    # print(str(
    # i['id']))
    # print(i['keysArr'])
    coins[i[3]] =  str(i[-5])


# print(coins)

for i in coins:
    page = requests.get(f'https://coinmarketcap.com/currencies/{coins[i]}/historical-data/?start=[20201201]&end=[20210103]')
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find('script', id="__NEXT_DATA__", type="application/json")
    historical_data = json.loads(data.contents[0])
    # print(historical_data)
    quotes = historical_data['props']['initialState']['cryptocurrency']['quotes'][f'{i}']
    # print(quotes)
    

    # info = historical_data['props']['initialState']['cryptocurrency']['ohlcvHistorical'][i]


    # market_cap = []
    # volume = []
    # timestamp = []
    # name = []
    # symbol = []
    # slug = []




    print(quotes['p'])


    # for j in quotes:
    #     print(j)
    #     market_cap.append(j['quote']['USD']['market_cap'])
    #     volume.append(j['quote']['USD']['volume'])
    #     timestamp.append(j['quote']['USD']['timestamp'])
    #     name.append(info['name'])
    #     symbol.append(info['symbol'])
    #     slug.append(coins[i])


    # df = pd.DataFrame(columns=['marketcap', 'volume', 'timestamp', 'name', 'symbol', 'slug'])

    # df['marketcap'] = market_cap
    # df['volume'] = volume
    # df['timestamp'] = timestamp
    # df['name'] = name
    # df['symbol'] = symbol
    # df['slug'] = slug

    break



# print(df)
