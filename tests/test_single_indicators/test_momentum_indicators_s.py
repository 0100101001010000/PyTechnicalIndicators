from src.PyTechnicalIndicators.Single.momentum_indicators import rate_of_change, on_balance_volume


def test_rate_of_change_increase():
    # Where current > previous
    current_close = 110
    previous_close = 100
    roc = rate_of_change(current_close_price=current_close, previous_close_price=previous_close)
    assert roc == 10


def test_rate_of_change_decrease():
    # Where current < previous
    current_close = 120
    previous_close = 150
    roc = rate_of_change(current_close_price=current_close, previous_close_price=previous_close)
    assert roc == -20


def test_rate_of_change_equal():
    # Where current = previous
    current_close = 100
    previous_close = 100
    roc = rate_of_change(current_close_price=current_close, previous_close_price=previous_close)
    assert roc == 0


def test_on_balance_volume_current_price_greater():
    obv = on_balance_volume(110, 100, 1000, 1500)
    assert obv == 2500


def test_on_balance_volume_prices_equal():
    obv = on_balance_volume(100, 100, 1000, 1500)
    assert obv == 1500


def test_on_balance_volume_previous_price_greater():
    obv = on_balance_volume(100, 110, 1000, 1500)
    assert obv == 500
