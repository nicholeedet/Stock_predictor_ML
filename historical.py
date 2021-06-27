import json
import requests
import pandas as pd
from pprint import pprint

def get_historical(ticker="AAPL"):
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?apikey=14f90359650cd4c61f0f33af0a7564d6"
    result = requests.get(url).json()
    df = pd.DataFrame(result['historical'])
    print(result['symbol'])
    print(df.head())
    print(df.shape)
    print(df.iloc[0])

get_historical("AAPL")