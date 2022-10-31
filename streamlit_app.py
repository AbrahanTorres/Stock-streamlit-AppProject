import streamlit as st
from vega_datasets import data
import chart
import yfinance as yf

def space(num_lines=1):
    '''This function adds empty lines to the Streamlit app'''
    for _ in range(num_lines):
        st.write("")

st.set_page_config(layout="centered", page_icon="📈", page_title="Stock Historical Prices & Data")

# Plot part using yfinance

st.title("📈 Stock Historical Prices & Data")
tickers = ("GOOGL", "AAPL", "MSFT", "TSLA", "NFLX", "IBM", "AMZN")
yahoo_data = yf.download(tickers, "2015-1-1", "2022-10-30")
yahoo_data = yahoo_data[("Close")]
st.line_chart(yahoo_data)
#st.write(yahoo_data)

# Plot selection part using vega_datasets

source = data.stocks()
all_symbols = source.symbol.unique()
symbols = st.multiselect("Choose stocks to plot below", all_symbols, all_symbols[:3])

space(1)

source = source[source.symbol.isin(symbols)]
chart = chart.get_chart(source)
st.altair_chart(chart, use_container_width=True)


space(2)




 