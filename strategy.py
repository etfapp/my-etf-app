
def recommend_strategy(vix: float, rsi_median: float) -> str:
    if vix > 25 or rsi_median > 70:
        return "保守"
    elif 20 < vix <= 25 or 50 < rsi_median <= 70:
        return "平衡"
    else:
        return "積極"
