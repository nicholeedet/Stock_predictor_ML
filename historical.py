import json
import requests
import pandas as pd
from pprint import pprint

from requests.models import DecodeError
from config import api_keys, password
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# Connecting to Database
connection_string = f"root:{password}@stock-predictor-ml-db.c3dvcigvu6ok.us-east-2.rds.amazonaws.com:5432/postgres"
engine = create_engine(f'postgresql://{connection_string}')

def get_tickers():
    df = pd.read_sql_query('select * from ticker', con=engine)
    new_df = df['name'] + " "  + df['symbol']
    return new_df.tolist()

def get_historical(ticker="AAPL"):
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?apikey={api_keys[0]}"
    result = requests.get(url).json()
    df = pd.DataFrame(result['historical'])
    print(result['symbol'])
    print(df.head())
    print(df.shape)
    print(df.iloc[0])
    df = df[["date","open","high","low","close"]]
    df.to_csv("./Historical_Data/historical_FB.csv",index=False)

def get_historical_(ticker):
    df = pd.read_sql_query('select * from ticker', con=engine)
    id = df[df['symbol']==ticker]['stock_id'].values[0] # returning ID for the specified ticker(symbol)
    df = pd.read_sql_query(f'select * from stock WHERE stock_id = {id}', con=engine)
    df = df.iloc[::-1]
    df.drop(['id', 'stock_id'], axis=1,inplace=True)
    print(df)


get_historical_("AAPL")
