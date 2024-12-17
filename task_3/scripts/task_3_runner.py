import sys
import os

# Add the `src` directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from data_loader import load_stock_data, load_news_data
from news_analysis import calculate_sentiment
from correlation import align_datasets, calculate_correlation
from visualization import plot_correlation_scatter

# File paths for your data
news_file = r"C:\Users\kingsta\Desktop\data\raw_analyst_ratings.csv"
stock_file = r"C:\Users\kingsta\Desktop\week_1\task_3\data\AAPL_historical_data.csv"

# Load your data
news_data = load_news_data(news_file)
stock_data = load_stock_data(stock_file)

# Perform sentiment analysis on your news headlines
news_data['sentiment'] = calculate_sentiment(news_data['headline'])

# Align datasets by date and calculate correlation
aligned_data = align_datasets(news_data, stock_data)
correlation = calculate_correlation(aligned_data)

# Print correlation results
print("Correlation:\n", correlation)

# Visualize correlation between sentiment and stock returns
plot_correlation_scatter(aligned_data, 'sentiment', 'daily_return', "Sentiment vs Stock Returns")
