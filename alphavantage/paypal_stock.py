import pandas as pd
import requests
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()
api_key= os.getenv("API_KEY")
url= f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=PYPL&apikey={api_key}'

response= requests.get(url)

data= response.json()

time_series= data.get("Weekly Adjusted Time Series", {})
df= pd.DataFrame.from_dict(time_series, orient="index")
df.reset_index(inplace=True)
df.rename(columns={
    "index": "date",
    "1. open": "open",
    "2. high": "high",
    "3. low": "low",
    "4. close": "close",
    "5. adjusted close": "adjusted_close",
    "6. volume": "volume",
    "7. dividend amount": "dividend_amount"
}, inplace=True)

df.drop(columns= "dividend_amount", inplace= True)

df["date"] = pd.to_datetime(df["date"])
df[["open", "high", "low", "close"]] = df[["open", "high", "low", "close"]].astype(float)
df["volume"] = df["volume"].astype(int)

df.to_csv("pypl_weekly_adjusted.csv", index=True, index_label= "id")
