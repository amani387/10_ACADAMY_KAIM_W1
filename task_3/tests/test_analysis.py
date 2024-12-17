from src.news_analysis import calculate_sentiment
from src.correlation import calculate_correlation

def test_calculate_sentiment():
    headlines = ["Stock market crashes", "Economy is booming"]
    sentiments = calculate_sentiment(headlines)
    assert len(sentiments) == 2, "Sentiment analysis should return correct number of results"

def test_calculate_correlation():
    # Mock data
    data = {
        'sentiment': [0.1, -0.2, 0.3],
        'daily_return': [0.01, -0.03, 0.05]
    }
    correlation = calculate_correlation(pd.DataFrame(data))
    assert 'sentiment' in correlation.columns, "Correlation output should include sentiment"
