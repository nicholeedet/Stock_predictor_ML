import json
import requests
import pandas as pd
from pprint import pprint

from requests.models import DecodeError
from config import api_keys, password
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# Connecting to Database
connection_string = f"ofygklqv:{password}@batyr.db.elephantsql.com:5432/ofygklqv"
engine = create_engine(f'postgresql://{connection_string}', pool_size=2, pool_recycle=1200, connect_args={'connect_timeout': 10},
client_encoding="utf8", pool_pre_ping=True)

def get_tickers():
    df = pd.read_sql_query('select * from ticker', con=engine)
    new_df = df['name'] + " "  + df['symbol']
    return new_df.tolist()

def get_historical_(ticker="AAPL"):
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?apikey={api_keys[0]}"
    result = requests.get(url).json()
    df = pd.DataFrame(result['historical'])
    print(result['symbol'])
    print(df.head())
    print(df.shape)
    print(df.iloc[0])
    df = df[["date","open","high","low","close"]]
    df.to_csv("./Historical_Data/historical_FB.csv",index=False)

def get_historical(ticker):
    df = pd.read_sql_query('select * from ticker', con=engine)
    id = df[df['symbol']==ticker]['stock_id'].values[0] # returning ID for the specified ticker(symbol)
    df = pd.read_sql_query(f'select * from stock WHERE stock_id = {id}', con=engine)
    df = df.iloc[::-1]
    df.drop(['id', 'stock_id'], axis=1,inplace=True)
    df.rename(columns={"date": "time","close":"value"}, inplace=True)
    df = df[["time","value"]]
    df[["value"]] = df[["value"]].astype(float)
    result = df.to_json(orient="records")
    parsed = json.loads(result)
    return (parsed) 


get_historical("AAPL")

def get_descriptions():
    tickers =["TSLA","AAPL","AMZN","MSFT","NIO","NVDA","MRNA","NKLA","FB","AMD"]
    descriptions = []
    for ticker in tickers:
        url = f"https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey=01220a885b2dd443a37bbefadc5022e2"
        result = requests.get(url).json()
        descriptions.append((ticker,result[0]['description']))
    print(descriptions)