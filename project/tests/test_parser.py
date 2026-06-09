from data_feed.binance_parser import parse_binance_kline_message

def test_parser_ignores_open_kline():
    raw_data = {
        "s" : "BTCUSDT",
        "k" : {
            "x" : False,
            "c" : "118.0",
            "v" : "5.5",
            "T" : 123456789
        }

    }
    assert parse_binance_kline_message(raw_data) is None

def test_parser_returns_event_for_closed_kline():
    raw_data = {
        "s" : "BTCUSDT",
        "k" : {
            "x" : True,
            "c" : "118.0",
            "v" : "5.5",
            "T" : 123456789
        }
    }
    event = parse_binance_kline_message(raw_data)

    assert event["close_price"] == 118.0
    assert event["volume"] == 5.5
    assert event["close_time_ms"] == 123456789
    assert event["closed"] is True