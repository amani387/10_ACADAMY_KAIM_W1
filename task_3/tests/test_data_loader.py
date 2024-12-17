from src.data_loader import load_stock_data, load_news_data

def test_load_stock_data():
    data = load_stock_data("data/AAPL_historical_data.csv")
    assert not data.empty, "Stock data should not be empty"

def test_load_news_data():
    data = load_news_data("data/news_data.csv")
    assert not data.empty, "News data should not be empty"
