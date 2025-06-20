
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from urllib.parse import parse_qs

st.set_page_config(page_title="技術圖表", layout="wide")

# 取得網址中的參數
query_params = st.query_params
symbol = query_params.get("symbol", None)

if not symbol:
    st.warning("請從清單點選 ETF 查看技術圖表")
    st.stop()

st.title(f"📈 技術圖表：{symbol}")

# 抓取資料
df = yf.download(symbol + ".TW", period="6mo", interval="1d")

if df.empty:
    st.error("無法取得資料，請確認代碼正確")
    st.stop()

# 計算技術指標
df["MA20"] = df["Close"].rolling(window=20).mean()
df["MA60"] = df["Close"].rolling(window=60).mean()
df["20_STD"] = df["Close"].rolling(window=20).std()
df["Upper"] = df["MA20"] + (2 * df["20_STD"])
df["Lower"] = df["MA20"] - (2 * df["20_STD"])

delta = df["Close"].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(14).mean()
avg_loss = loss.rolling(14).mean()
rs = avg_gain / avg_loss
df["RSI"] = 100 - (100 / (1 + rs))

ema12 = df["Close"].ewm(span=12, adjust=False).mean()
ema26 = df["Close"].ewm(span=26, adjust=False).mean()
df["MACD"] = ema12 - ema26
df["Signal"] = df["MACD"].ewm(span=9, adjust=False).mean()

# 畫圖
fig = go.Figure()

fig.add_trace(go.Candlestick(x=df.index,
                             open=df["Open"], high=df["High"],
                             low=df["Low"], close=df["Close"],
                             name="K線"))

fig.add_trace(go.Scatter(x=df.index, y=df["MA20"], mode='lines', name='MA20'))
fig.add_trace(go.Scatter(x=df.index, y=df["MA60"], mode='lines', name='MA60'))
fig.add_trace(go.Scatter(x=df.index, y=df["Upper"], mode='lines', name='上布林'))
fig.add_trace(go.Scatter(x=df.index, y=df["Lower"], mode='lines', name='下布林'))

fig.update_layout(title=f"{symbol} 技術圖表",
                  xaxis_rangeslider_visible=False)

st.plotly_chart(fig, use_container_width=True)

# RSI 圖
rsi_fig = go.Figure()
rsi_fig.add_trace(go.Scatter(x=df.index, y=df["RSI"], name="RSI"))
rsi_fig.update_layout(title="RSI 指標", yaxis=dict(range=[0, 100]))
st.plotly_chart(rsi_fig, use_container_width=True)

# MACD 圖
macd_fig = go.Figure()
macd_fig.add_trace(go.Scatter(x=df.index, y=df["MACD"], name="MACD"))
macd_fig.add_trace(go.Scatter(x=df.index, y=df["Signal"], name="Signal"))
macd_fig.update_layout(title="MACD 指標")
st.plotly_chart(macd_fig, use_container_width=True)
