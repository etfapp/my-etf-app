import streamlit as st
import pandas as pd
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.data_loader import load_watchlist, save_watchlist, load_etf_summary

st.title("⭐ 自選清單 + 水位計算機 + 存股模擬器")

# === 顯示目前自選清單 ===
df_watch = load_watchlist()
st.subheader("📋 目前自選清單")
st.dataframe(df_watch, use_container_width=True)

# === 新增自選清單項目 ===
st.subheader("➕ 新增 ETF")
new_code = st.text_input("輸入 ETF 代碼（例如 0050）", "")
if st.button("加入自選清單") and new_code:
    if new_code not in df_watch["代碼"].astype(str).values:
        df_watch.loc[len(df_watch)] = [new_code]
        save_watchlist(df_watch)
        st.success(f"{new_code} 已新增")
        st.rerun()
    else:
        st.warning("此代碼已存在於自選清單中")

# === 刪除清單項目 ===
st.subheader("🗑️ 刪除 ETF")
if not df_watch.empty:
    remove_code = st.selectbox("選擇要刪除的代碼", df_watch["代碼"])
    if st.button("刪除選擇項目"):
        df_watch = df_watch[df_watch["代碼"] != remove_code]
        save_watchlist(df_watch)
        st.success(f"{remove_code} 已刪除")
        st.rerun()

# === 水位計算機 + 存股模擬器 ===
st.subheader("💧 水位計算機 + 存股模擬器")

if df_watch.empty:
    st.info("請先加入至少一檔 ETF 至自選清單。")
else:
    etf_all = load_etf_summary()
    selected = etf_all[etf_all["代碼"].astype(str).isin(df_watch["代碼"].astype(str))].copy()

    if selected.empty:
        st.warning("自選清單中代碼無法在 ETF 總表中比對，請確認代碼正確。")
    else:
        cash = st.number_input("請輸入可佈局金額（元）", min_value=0, step=1000)
        etf_count = len(selected)

        # 建立位階分數（殖利率高代表位階低）
        selected["位階分數"] = selected["殖利率"].rank(ascending=False)
        total_score = selected["位階分數"].sum()

        # 計算建議金額與股數
        selected["建議投入金額"] = (selected["位階分數"] / total_score * cash).round(0)
        selected["預估可買股數"] = (selected["建議投入金額"] / selected["價格"]).fillna(0).astype(int)

        st.markdown("### 📊 建議分配結果")
        st.dataframe(selected[["代碼", "名稱", "殖利率", "價格", "建議投入金額", "預估可買股數"]], use_container_width=True)

st.markdown('---')
st.markdown('### 🔍 技術圖表快速查看')
if not watchlist_df.empty:
    df_for_chart = watchlist_df if 'watchlist_df' in locals() else pd.DataFrame()
    for i, row in df_for_chart.iterrows():
    st.markdown(f"📊 [{row['代碼']}](/chart?symbol={row['代碼']})", unsafe_allow_html=True)
