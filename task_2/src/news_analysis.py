from textblob import TextBlob

def calculate_sentiment(headlines):
    """Calculate sentiment polarity for a list of headlines."""
    return [TextBlob(headline).sentiment.polarity for headline in headlines]
