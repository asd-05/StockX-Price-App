import streamlit as st
import requests
import pandas as pd
import json
import plotly.express as px

st.set_page_config(
    initial_sidebar_state="auto",
    page_title="STOCKX Price",
)

st.markdown('''# **STOCKX Price App**
A simple stock market price app pulling price data from *Alpha Vantage API*.
''')


api_endpoint = 'https://www.alphavantage.co/query'
api_key = 'QMM8A5DZQBGSCMZT'
function = 'TIME_SERIES_DAILY_ADJUSTED'
output_size = 'compact'


symbols = ['AAPL','TSLA', 'IBM', 'MSFT', 'META', 'GOOG', 'TOP', 'ASML', 'AMZN']

symbol = st.selectbox('Select a stock symbol', symbols)

col1_selection = st.sidebar.selectbox('Price 1', symbols, list(symbols).index('AAPL') )
col2_selection = st.sidebar.selectbox('Price 2', symbols, list(symbols).index('TSLA') )
col3_selection = st.sidebar.selectbox('Price 3', symbols, list(symbols).index('IBM') )
col4_selection = st.sidebar.selectbox('Price 4', symbols, list(symbols).index('MSFT') )
col5_selection = st.sidebar.selectbox('Price 5', symbols, list(symbols).index('META') )
col6_selection = st.sidebar.selectbox('Price 6', symbols, list(symbols).index('GOOG') )
col7_selection = st.sidebar.selectbox('Price 7', symbols, list(symbols).index('TOP') )
col8_selection = st.sidebar.selectbox('Price 8', symbols, list(symbols).index('ASML') )
col9_selection = st.sidebar.selectbox('Price 9', symbols, list(symbols).index('AMZN') )


response = requests.get(f'{api_endpoint}?function={function}&symbol={symbol}&outputsize={output_size}&apikey={api_key}')

if response.status_code == 200:
    
    data = response.json()

    df = pd.DataFrame(data['Time Series (Daily)']).transpose()
    df.index.name = 'date'
    df.columns = ['open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'dividend_amount', 'split_coefficient']
    df.index = pd.to_datetime(df.index)

    st.write(f"Daily Adjusted Closing Prices for {symbol}")
    st.write(df[['open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'dividend_amount']])
    
else:
    st.write("Error: Failed to retrieve data from API")

