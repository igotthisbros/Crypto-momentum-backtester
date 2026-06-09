def parse_binance_kline_message(raw_message):
    kline = raw_message["k"]
    
    if not kline["x"]:
        return None
    
    return {
        "close_price" : float(kline["c"]),
        "volume" : float(kline["v"]),
        "close_time_ms" : int(kline["T"]),
        "closed" : kline["x"]
    }