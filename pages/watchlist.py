import streamlit as st
import pandas as pd
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.data_loader import load_watchlist, save_watchlist

st.title("⭐ 自選清單")

df = load_watchlist()

# 顯示表格
st.subheader("目前自選清單")
st.dataframe(df, use_container_width=True)

# 新增功能
st.subheader("新增 ETF")
new_code = st.text_input("輸入 ETF 代碼（例如 0050）", "")
if st.button("加入自選清單") and new_code:
    if new_code not in df["代碼"].values:
        df.loc[len(df)] = [new_code]
        save_watchlist(df)
        st.success(f"{new_code} 已新增")
        st.rerun()
    else:
        st.warning("此代碼已存在於自選清單中")

# 刪除功能
st.subheader("刪除 ETF")
remove_code = st.selectbox("選擇要刪除的代碼", df["代碼"].unique() if not df.empty else [])
if st.button("刪除選擇項目"):
    df = df[df["代碼"] != remove_code]
    save_watchlist(df)
    st.success(f"{remove_code} 已刪除")
    st.rerun()