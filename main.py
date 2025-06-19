import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st
import pages.etf_summary as etf_summary
import pages.watchlist as watchlist
import pages.heat_zone as heat_zone
import pages.dynamic_list as dynamic_list
import pages.chart as chart
import pages.calculator as calculator

# 設定頁面標題與配置
st.set_page_config(page_title="MyETF 助手", layout="wide")
st.sidebar.title("📊 功能選單")

# 頁面選單
page = st.sidebar.radio("請選擇功能", [
    "ETF總表", "自選清單", "升溫區", "動態清單", "技術圖表", "計算工具"
])

# 導向對應頁面
if page == "ETF總表":
    etf_summary.app()
elif page == "自選清單":
    watchlist.app()
elif page == "升溫區":
    heat_zone.app()
elif page == "動態清單":
    dynamic_list.app()
elif page == "技術圖表":
    chart.app()
elif page == "計算工具":
    calculator.app()