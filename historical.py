import json
import requests
import pandas as pd
from pprint import pprint
from config import keys

def get_historical(ticker="AAPL"):
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?apikey={keys[0]}"
    result = requests.get(url).json()
    df = pd.DataFrame(result['historical'])
    print(result['symbol'])
    print(df.head())
    print(df.shape)
    print(df.iloc[0])
    df = df[["date","open","high","low","close"]]
    df.to_csv("./Historical_Data/historical_FB.csv",index=False)

get_historical("FB")