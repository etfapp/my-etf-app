
import streamlit as st
import pandas as pd
import os
from datetime import datetime
from utils.strategy import recommend_strategy
from utils.data_loader import load_summary_data, load_watchlist

st.set_page_config(page_title="首頁總覽", layout="wide")
st.title("📊 MyETF 助手：首頁總覽")

# 顯示資料更新時間
update_file = "data/update_status.csv"
if os.path.exists(update_file):
    update_df = pd.read_csv(update_file)
    last_update = update_df['update_time'].values[0]
    st.success(f"✅ 資料最近更新時間：{last_update}")
else:
    st.warning("⚠️ 尚未取得更新狀態資料")

# 顯示策略建議與市場溫度
st.subheader("📌 今日市場溫度與建議策略")
strategy = recommend_strategy()
st.info(f"今日建議策略為：**{strategy}**")

# 動態清單摘要
try:
    df = load_summary_data()
    dynamic_list = df[df['技術燈號'] == '低'].reset_index(drop=True)
    st.subheader("📈 動態清單摘要")
    st.metric(label="建議佈局標的數", value=f"{len(dynamic_list)} 檔")
except:
    st.warning("無法載入動態清單資料")

# 升溫區摘要
try:
    hot_list = df[df['技術燈號'] == '高'].reset_index(drop=True)
    st.subheader("🚨 升溫區摘要")
    st.metric(label="升溫警示標的數", value=f"{len(hot_list)} 檔")
except:
    st.warning("無法載入升溫區資料")

# 手動更新按鈕
st.subheader("🔄 手動更新 ETF 資料")
if st.button("立即更新"):
    result = os.system("python utils/update_data.py")
    if result == 0:
        st.success("✅ 資料更新成功")
    else:
        st.error("❌ 資料更新失敗，請檢查 update_data.py 是否正常")
