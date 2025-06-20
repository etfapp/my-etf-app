
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title("📈 ETF 技術圖表")

symbol = st.query_params.get("symbol", "")
if not symbol:
    st.warning("未指定 symbol 參數")
    st.stop()

st.subheader(f"技術圖表：{symbol}")

try:
    data = yf.download(symbol, period="6mo", interval="1d")
    if data.empty:
        st.error("找不到資料")
    else:
        fig = go.Figure()
        fig.add_trace(go.Candlestick(x=data.index,
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close'],
                                     name='K線'))

        data["MA5"] = data["Close"].rolling(window=5).mean()
        data["MA20"] = data["Close"].rolling(window=20).mean()
        fig.add_trace(go.Scatter(x=data.index, y=data["MA5"], mode="lines", name="MA5"))
        fig.add_trace(go.Scatter(x=data.index, y=data["MA20"], mode="lines", name="MA20"))

        st.plotly_chart(fig, use_container_width=True)
except Exception as e:
    st.error(f"資料載入失敗：{e}")
