import pandas as pd

def align_data(news_data, stock_data):
    """Align news and stock data by date."""
    news_data['date'] = pd.to_datetime(news_data['date'])
    stock_data['date'] = pd.to_datetime(stock_data.index)
    return pd.merge(news_data, stock_data, on='date', how='inner')

def calculate_correlation(data):
    """Calculate correlation between sentiment and stock returns."""
    return data[['sentiment', 'daily_return']].corr()
