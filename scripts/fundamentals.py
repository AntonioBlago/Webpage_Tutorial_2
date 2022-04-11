import yfinance as yf
import pandas as pd
import scripts.plotly_layouts as ply
import datetime as dt

def get_dividends(ticker):

    ticker = yf.Ticker(ticker)

    ## Dividends
    dividends = ticker.get_dividends()
    dividends = dividends.to_frame()
    dividends = dividends.reset_index()
    dividends["year"] = dividends["Date"].dt.year
    dividends = dividends.groupby("year")["Dividends"].sum()
    dividends = dividends.to_frame()
    dividends = dividends.reset_index()

    return ply.create_plotly(dividends)

if __name__ == '__main__':
    get_dividends("AAPL")