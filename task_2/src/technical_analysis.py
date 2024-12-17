import talib

def calculate_sma(data, timeperiod=20):
    return talib.SMA(data, timeperiod)

def calculate_rsi(data, timeperiod=14):
    return talib.RSI(data, timeperiod)

def calculate_macd(data):
    macd, macd_signal, macd_hist = talib.MACD(data)
    return macd, macd_signal, macd_hist
