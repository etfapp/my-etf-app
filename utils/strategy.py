
def get_strategy_recommendation(vix_index: float, rsi_index: float) -> str:
    '''
    根據 VIX 與 RSI 指標提供策略建議：
    - 保守型：市場高風險（VIX 高，RSI 高）
    - 穩健型：中性
    - 積極型：市場偏低檔（VIX 低，RSI 低）
    '''
    if vix_index > 25 or rsi_index > 70:
        return "保守型"
    elif vix_index < 15 and rsi_index < 30:
        return "積極型"
    else:
        return "平衡型"
