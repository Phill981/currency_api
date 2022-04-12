import requests
import pandas as pd
import datetime as dt
from forex_python.converter import CurrencyRates

def get_crypto_price_in_usd(symbol):
    exchange = 'USD'
    start_date = dt.datetime.today().strftime('%Y-%m-%d')
    api_key = 'JZE3WM3TYROCR1JU'
    api_url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market={exchange}&apikey={api_key}'
    raw_df = requests.get(api_url).json()
    df = pd.DataFrame(raw_df['Time Series (Digital Currency Daily)']).T
    df = df.rename(columns = {'1a. open (USD)': 'open', '2a. high (USD)': 'high', '3a. low (USD)': 'low', '4a. close (USD)': 'close', '5. volume': 'volume'})
    for i in df.columns:
        df[i] = df[i].astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.iloc[::-1].drop(['1b. open (USD)', '2b. high (USD)', '3b. low (USD)', '4b. close (USD)', '6. market cap (USD)'], axis = 1)
    if start_date:
        df = df[df.index >= start_date]
    return df["close"].values[0]

def get_fiat_price_is(from_curency, to_curreny):
    rates = CurrencyRates()
    return rates.get_rates(from_curency)[to_curreny.upper()]
