import streamlit as st
import pandas as pd
from utils.data_loader import load_watchlist, save_watchlist

st.title("💧 水位計算機 + 📈 存股模擬器")

# 策略模式選擇
strategy_mode = st.selectbox("請選擇策略模式", ["保守型", "平衡型", "積極型"])

# 風險參數對應投入比例
strategy_cash_ratio = {
    "保守型": 0.3,
    "平衡型": 0.5,
    "積極型": 0.8
}

# 1️⃣ 水位計算機
st.subheader("💧 水位計算機")
cash = st.number_input("請輸入目前現金（元）", min_value=0, step=1000)
ratio = strategy_cash_ratio[strategy_mode]
suggested_investment = int(cash * ratio)
st.info(f"📊 根據 {strategy_mode} 策略，建議投入比例為 {int(ratio*100)}%")
st.success(f"💰 建議投入金額：{suggested_investment:,} 元")

# 2️⃣ 存股模擬器
st.subheader("📈 存股模擬器")

df = load_watchlist()
if df.empty or "目前價格" not in df.columns:
    st.warning("尚未設定自選清單或缺乏價格資料")
else:
    df = df.copy()
    count = st.number_input("請輸入想配置的標的數量", min_value=1, max_value=len(df), value=len(df))

    # 分配資金（均分）
    allocated = suggested_investment // count
    df["建議投入金額"] = allocated
    df["建議股數"] = (allocated / pd.to_numeric(df["目前價格"], errors="coerce")).fillna(0).astype(int)

    st.markdown(f"根據佈局金額 **{suggested_investment:,} 元** 與標的數量 **{count} 檔**，以下為配置結果：")
    st.dataframe(df[["代碼", "名稱", "目前價格", "建議投入金額", "建議股數"]], use_container_width=True)

    if st.button("✅ 儲存結果至自選清單"):
        save_watchlist(df)
        st.success("已儲存配置結果至 watchlist.csv，請至自選清單查看。")