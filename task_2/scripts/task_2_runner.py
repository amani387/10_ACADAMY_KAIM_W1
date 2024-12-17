import sys
import os

# Add the src folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from data_loader import load_stock_data
from technical_analysis import calculate_sma, calculate_rsi, calculate_macd
from visualization import plot_stock_data

# Load data from a local file instead of yfinance
file_path = r"C:\Users\kingsta\Desktop\week_1\task_2\data\AAPL_historical_data.csv"
import pandas as pd
data = pd.read_csv(file_path)

# Perform analysis
data['SMA'] = calculate_sma(data['Close'])
data['RSI'] = calculate_rsi(data['Close'])
data['MACD'], data['MACD_signal'], _ = calculate_macd(data['Close'])

# Visualize results
plot_stock_data(data, 'Close', "Closing Prices")
plot_stock_data(data, 'SMA', "20-Day SMA")
plot_stock_data(data, 'RSI', "RSI")
