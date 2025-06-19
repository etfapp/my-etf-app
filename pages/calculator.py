import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st

def app():
    st.title("💧 水位計算機＋存股計算機")

    # 使用者輸入現金金額
    cash = st.number_input("請輸入可用現金金額（元）", min_value=0, value=100000, step=1000)

    # 選擇策略模式
    strategy = st.selectbox("選擇投資策略模式", ["保守型", "平衡型", "積極型"])

    # 根據策略設定建議投入比例
    ratio = {
        "保守型": 0.2,
        "平衡型": 0.5,
        "積極型": 0.8
    }[strategy]

    # 計算建議投入金額
    invest_amt = int(cash * ratio)
    st.success(f"🔎 依據「{strategy}」策略，建議投入金額：{invest_amt:,} 元")

    st.markdown("---")
    st.subheader("📊 存股計算機")

    # 模擬 ETF 清單（後續串接真實自選清單）
    example_etfs = ["0050", "00878", "00929"]
    selected_etfs = st.multiselect("請選擇欲投資之 ETF", example_etfs, default=example_etfs)

    # 根據 ETF 數量平均分配投入金額
    if selected_etfs:
        avg_amt = invest_amt // len(selected_etfs)
        st.markdown("#### 💡 每檔平均可投入金額與假設股數：")
        for etf in selected_etfs:
            price = 20  # 假設每股價格，後續串接真實價格
            shares = avg_amt // price
            st.write(f"{etf}：可投入 {avg_amt:,} 元，約可買入 {shares} 股（假設單價 {price} 元）")
    else:
        st.info("請至少選擇一檔 ETF 以進行存股計算")
