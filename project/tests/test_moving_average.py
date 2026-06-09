from strategies.moving_average import MovingAverageStrategy

def make_events(price, timestamp=123):
    return  {
        "close_price": price,
        "volume": 1.0,
        "close_time_ms": timestamp,
        "closed": True,
    }


def test_moving_strategy_ignores_sell_before_buy():
    strategy = MovingAverageStrategy(short_window=2,long_window=3)

    assert strategy.on_event(make_events(100)) is None
    assert strategy.on_event(make_events(110)) is None
    result = strategy.on_event(make_events(105))
    assert result['signal'] == "SELL_IGNORED"

def test_moving_strategy_buy_when_short_ma_below_long_ma():
    strategy = MovingAverageStrategy(short_window=2,long_window=3)
    

    assert strategy.on_event(make_events(105)) is None
    assert strategy.on_event(make_events(102)) is None
    result = strategy.on_event(make_events(100))
    assert result['signal'] == "BUY"
    