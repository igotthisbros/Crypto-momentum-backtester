from utils.indicators import RollingMean


def test_rolling_mean_waits_until_full():
    test = RollingMean(3)

    assert test.update(1) is None
    assert test.update(2) is None
    assert test.update(3) == 2.0
    assert test.update(4) == 3.0
