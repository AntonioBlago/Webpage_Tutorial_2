import yfinance as yf
import pandas as pd
import scripts.plotly_layouts as ply
import datetime as dt
import datapane as dp

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

def upload_to_datapane(plot, title):
    report = dp.Report(dp.Plot(plot))  # Create a report
    report.upload(name=title, open=True, visibility='PUBLIC')

    print("success")

    return True


if __name__ == '__main__':
    plot = get_dividends("AAPL")
    upload_to_datapane(plot, "AAPL Dividends Plot")