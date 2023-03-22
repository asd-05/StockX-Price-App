import streamlit as st
import requests
import pandas as pd
import json

st.markdown('''# **STOCKX Price App**
A simple stock market price app pulling price data from *Alpha Vantage API*.
''')

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=QMM8A5DZQBGSCMZT'
r = requests.get(url)
data = r.json()

params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "IBM",
    "interval": "5min",
}

time_series = data["Time Series (5min)"]
df = pd.DataFrame.from_dict(time_series, orient="index")
df.index = pd.to_datetime(df.index)
st.write(df)


# st.write(data)