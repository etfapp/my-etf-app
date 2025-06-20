
import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

st.set_page_config(page_title="📈 技術圖表", layout="wide")
st.title("📈 ETF 技術圖表")

query_params = st.query_params
symbol = query_params.get("symbol", "")

if not symbol:
    st.warning("請從其他頁面點選 ETF 以載入技術圖。")
    st.stop()

etf_code = symbol + ".TW" if ".TW" not in symbol else symbol
df = yf.download(etf_code, period="6mo", interval="1d")

if df.empty:
    st.error("無法取得資料，請確認代碼是否正確")
    st.stop()

st.subheader(f"ETF: {symbol}")

# 繪製 K 線圖與均線
fig = go.Figure()
fig.add_trace(go.Candlestick(
    x=df.index,
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    name='K線圖'
))

df['MA5'] = df['Close'].rolling(window=5).mean()
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA60'] = df['Close'].rolling(window=60).mean()

fig.add_trace(go.Scatter(x=df.index, y=df['MA5'], mode='lines', name='5MA'))
fig.add_trace(go.Scatter(x=df.index, y=df['MA20'], mode='lines', name='20MA'))
fig.add_trace(go.Scatter(x=df.index, y=df['MA60'], mode='lines', name='60MA'))

fig.update_layout(title=f"{symbol} 技術分析圖", xaxis_rangeslider_visible=False)
st.plotly_chart(fig, use_container_width=True)
