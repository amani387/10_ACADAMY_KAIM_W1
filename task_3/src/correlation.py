import pandas as pd

def align_datasets(news_data, stock_data):
    """Align datasets by date."""
    
    # Try to parse the news date column with proper format
    news_data['date'] = pd.to_datetime(news_data['date'], errors='coerce')
    
    # If needed, remove timezone info
    news_data['date'] = news_data['date'].dt.tz_localize(None)
    
    # Ensure stock data date column is in datetime format
    stock_data['date'] = pd.to_datetime(stock_data['Date'], errors='coerce')
    
    # Calculate daily return for stock data
    stock_data['daily_return'] = stock_data['Close'].pct_change()
    
    # Merge datasets on 'date' and return
    return pd.merge(news_data, stock_data, on='date', how='inner')



def calculate_correlation(data):
    """Calculate Pearson correlation between sentiment and stock returns."""
    return data[['sentiment', 'daily_return']].corr()




