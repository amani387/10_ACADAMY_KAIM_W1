import yfinance as yf
import pandas as pd

def load_stock_data(tickers, start_date, end_date):
    """Fetch stock data using yfinance."""
    return yf.download(tickers, start=start_date, end=end_date, group_by="ticker")

def load_news_data(filepath):
    """Load news data from a CSV or other file format."""
    return pd.read_csv(filepath)

