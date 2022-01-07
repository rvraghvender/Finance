import numpy as np
import pandas as pd
import requests
import yfinance as yf
import plotly.graph_objs as go
import time

class Currency_converter:

    #empty dict to store the conversion rates
    # rates = {}
    def __init__(self, url):
        jsonData = requests.get(url).json()

        # Extracting only the rates from the json data
        self.rates = jsonData["quotes"]


    # function to do a simple cross multiplication between the amount and the conversion rates
    def convert(self, from_currency, to_currency, amount):
        index = str.__add__(from_currency, to_currency)
        amount = amount * self.rates[index]
        return amount, self.rates[index]

   
  
url = 'http://api.currencylayer.com/live?access_key=a08153486e03a01b0bbdc7635656a08a'


def crypto_analysis():
    conversion = Currency_converter(url)

    # Get Bitcoin data
    # Interval sample =  “1m”, “2m”, “5m”, “15m”, “30m”, “60m”, “90m”, “1h”, “1d”, “5d”, “1wk”, “1mo”, “3mo”
    # period sample = “1d”, “5d”, “1mo”, “3mo”, “6mo”, “1y”, “2y”, “5y”, “10y”, “ytd”, “max”

    data = yf.download(tickers='BTC-USD', period = '6mo', interval = '60m', group_by='tickers')


    #declare figure
    fig = go.Figure()

    #Candlestick
    fig.add_trace(go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], 
                name = 'market data'))

    # Last price
    CurrentPrice = conversion.convert('USD', 'EUR', float(data['Close'][-1]))


    # Add titles
    fig.update_layout(
        title=f'Bitcoin live share price evolution : {CurrentPrice[0]} EUR [Conversion Rate (USD2EUR) : {CurrentPrice[1]}]',
        yaxis_title='Bitcoin Price (kUS Dollars)')

    # X-Axes
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=6, label="6h", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    #Show
    fig.show()


if __name__ == '__main__':
    while True:
        crypto_analysis()
        break
        # time.sleep(10)

