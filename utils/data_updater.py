
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(series, short=12, long=26, signal=9):
    ema_short = series.ewm(span=short, adjust=False).mean()
    ema_long = series.ewm(span=long, adjust=False).mean()
    macd = ema_short - ema_long
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line

def update_etf_data(input_csv='data/etf_summary.csv', output_csv='data/etf_summary.csv'):
    try:
        df = pd.read_csv(input_csv)
        df["RSI"] = None
        df["MACD"] = None
        for idx, row in df.iterrows():
            symbol = str(row["代碼"])
            try:
                data = yf.download(f"{symbol}.TW", period="3mo", interval="1d", progress=False)
                if len(data) < 30:
                    continue
                close = data["Close"]
                rsi = calculate_rsi(close).iloc[-1]
                macd, signal = calculate_macd(close)
                last_macd = macd.iloc[-1]
                df.at[idx, "RSI"] = round(rsi, 2)
                df.at[idx, "MACD"] = round(last_macd, 2)
            except Exception as e:
                print(f"Error fetching {symbol}: {e}")
        df.to_csv(output_csv, index=False)
        print("ETF 資料已更新")
    except Exception as e:
        print("更新失敗：", e)

if __name__ == "__main__":
    update_etf_data()
