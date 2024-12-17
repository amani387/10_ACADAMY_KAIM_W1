from src.data_loader import load_news_data, load_stock_data
from src.news_analysis import calculate_sentiment
from src.correlation import align_data, calculate_correlation
from src.visualization import plot_correlation_scatter

# Load data
news_data = load_news_data("news.csv")
stock_data = load_stock_data(["AAPL"], "2023-01-01", "2023-12-31")['AAPL']

# Add sentiment and align data
news_data['sentiment'] = calculate_sentiment(news_data['headline'])
aligned_data = align_data(news_data, stock_data)

# Calculate and visualize correlation
correlation = calculate_correlation(aligned_data)
print(correlation)

plot_correlation_scatter(aligned_data, 'sentiment', 'daily_return')
