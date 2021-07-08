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
    df['time'] = df['time'].apply(lambda x: pd.Timestamp(x).timestamp())
    result = df.to_json(orient="records")
    parsed = json.loads(result)
    return (parsed) 

def get_descriptions():
    tickers =["TSLA","AAPL","AMZN","MSFT","NIO","NVDA","MRNA","NKLA","FB","AMD"]
    descriptions = []
    for ticker in tickers:
        url = f"https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey=14f90359650cd4c61f0f33af0a7564d6"
        result = requests.get(url).json()
        descriptions.append({"symbol":result[0]['symbol'],"name":result[0]['companyName'],"description":result[0]['description']})
    return(descriptions)

def get_predicted(ticker="AAPL"):
    df = pd.read_sql_query('select * from ticker', con=engine)
    id = df[df['symbol']==ticker]['stock_id'].values[0] # returning ID for the specified ticker(symbol)
    total_data =  pd.read_sql_query(f"select * from stock WHERE stock_id = {id}", con=engine)
    total_data = total_data.iloc[::-1]
    df = pd.read_sql_query(f'select * from predicted WHERE stock_id = {id}', con=engine)
    total_data.rename(columns={"date":"time", "close":'value'},inplace=True)
    total_data.filter(['time','value']) 
    total_data['time'] = total_data['time'].apply(lambda x: pd.Timestamp(x).timestamp())
    # obtaining predicted dataset length
    ln = len(df)
    #Obtaining training dataset
    train_values = total_data.iloc[:len(total_data)-ln,:]
    train_values= train_values.filter(['time','value'])
    # getting dates for test data
    test_values = total_data.tail(ln)
    test_values['close'] = df['close'].tolist()
    test_values['predictions'] = df['predictions'].tolist()
    test_values = test_values.filter(['time','close','predictions'])
    predicted = test_values[['time','predictions']]
    test_values = test_values.filter(['time','close'])
    test_values.rename(columns={"close":"value"},inplace=True)
    predicted.rename(columns={"predictions":"value"},inplace=True)
    result = train_values.to_json(orient="records")
    train = json.loads(result)
    result = test_values.to_json(orient="records")
    test = json.loads(result)
    result = predicted.to_json(orient="records")
    predicted_ = json.loads(result)
    return({"train":train,"test":test,"predicted":predicted_})