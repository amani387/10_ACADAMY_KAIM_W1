import pandas as pd

def load_stock_data(file_path):
    """Load stock data from CSV."""
    return pd.read_csv(file_path)

def load_news_data(file_path):
    """Load news data from CSV."""
    return pd.read_csv(file_path)
