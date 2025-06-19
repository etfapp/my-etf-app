import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

def plot_chart(ticker):
    df = yf.download(ticker + ".TW", period="6mo", interval="1d", progress=False)
    df.dropna(inplace=True)

    # 計算技術指標
    df["MA20"] = df["Close"].rolling(window=20).mean()
    df["Upper"] = df["MA20"] + 2 * df["Close"].rolling(window=20).std()
    df["Lower"] = df["MA20"] - 2 * df["Close"].rolling(window=20).std()
    df["RSI"] = 100 - (100 / (1 + df["Close"].pct_change().rolling(14).mean() / df["Close"].pct_change().rolling(14).std()))
    df["MACD"] = df["Close"].ewm(span=12).mean() - df["Close"].ewm(span=26).mean()
    df["Signal"] = df["MACD"].ewm(span=9).mean()

    # K線圖＋布林通道
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df["Open"], high=df["High"],
                                         low=df["Low"], close=df["Close"],
                                         name='K線')])
    fig.add_trace(go.Scatter(x=df.index, y=df["Upper"], line=dict(color='gray', width=1), name='布林上軌'))
    fig.add_trace(go.Scatter(x=df.index, y=df["Lower"], line=dict(color='gray', width=1), name='布林下軌'))
    fig.update_layout(title="K 線圖與布林通道", xaxis_title="日期", yaxis_title="價格")

    st.plotly_chart(fig, use_container_width=True)

    # MACD 圖
    st.subheader("MACD 指標")
    fig_macd = go.Figure()
    fig_macd.add_trace(go.Scatter(x=df.index, y=df["MACD"], name='MACD'))
    fig_macd.add_trace(go.Scatter(x=df.index, y=df["Signal"], name='Signal'))
    st.plotly_chart(fig_macd, use_container_width=True)

    # RSI 圖
    st.subheader("RSI 指標")
    fig_rsi = go.Figure()
    fig_rsi.add_trace(go.Scatter(x=df.index, y=df["RSI"], name='RSI'))
    fig_rsi.update_layout(yaxis_range=[0, 100])
    st.plotly_chart(fig_rsi, use_container_width=True)

def app():
    st.title("📈 ETF 技術圖表分析")
    etf_code = st.text_input("請輸入 ETF 代碼（例如：0050）", value="0050")

    if etf_code:
        plot_chart(etf_code.strip())
