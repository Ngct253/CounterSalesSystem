import pytest

# ==================== CORE FUNCTIONS ====================
def calculate_new_price(wac: float, margin: float) -> float:
    """
    New Price = WAC * (1 + margin / 100)
    """
    return wac * (1 + margin / 100)

def validate_margin(margin: float) -> bool:
    """
    Profit Margin phải >=30%
    """
    return margin >= 30.0

def validate_currency(value: float) -> bool:
    """
    Kiểm tra giá trị tiền tệ trong $0 - $999,999.99
    """
    return 0 <= value <= 999_999.99

# ==================== PROFIT MARGIN TEST CASES ====================
def test_ProfMar_001_valid_min_30():
    wac = 100.00
    margin = 30.0
    new_price = calculate_new_price(wac, margin)
    assert new_price == 130.00
    assert validate_margin(margin)
    assert validate_currency(new_price)

def test_ProfMar_002_invalid_below_30():
    wac = 100.00
    margin = 29.99
    new_price = calculate_new_price(wac, margin)
    assert new_price == pytest.approx(129.99, 0.01)
    assert not validate_margin(margin)
    assert validate_currency(new_price)

def test_ProfMar_003_valid_above_30_01():
    wac = 100.00
    margin = 30.01
    new_price = calculate_new_price(wac, margin)
    assert new_price == pytest.approx(130.01, 0.01)
    assert validate_margin(margin)
    assert validate_currency(new_price)

def test_ProfMar_004_high_margin_exceed_max():
    wac = 100.00
    margin = 999999
    new_price = calculate_new_price(wac, margin)
    assert new_price > 999_999.99
    assert not validate_currency(new_price)

def test_ProfMar_005_invalid_negative_margin():
    wac = 100.00
    margin = -50
    new_price = calculate_new_price(wac, margin)
    assert new_price == 50.00
    assert not validate_margin(margin)
    assert validate_currency(new_price)

def test_ProfMar_006_margin_zero():
    wac = 100.00
    margin = 0
    new_price = calculate_new_price(wac, margin)
    assert new_price == 100.00
    assert not validate_margin(margin)
    assert validate_currency(new_price)

def test_ProfMar_007_dat_on_off_in():
    wac = 100.00
    # ON: 30, OFF: 29,31, IN: 0
    test_values = [(0, False), (29, False), (30, True), (31, True)]
    for margin, valid in test_values:
        new_price = calculate_new_price(wac, margin)
        assert validate_margin(margin) == valid
        assert validate_currency(new_price)

def test_ProfMar_008_currency_min_zero():
    wac = 100.00
    margin = -100
    new_price = calculate_new_price(wac, margin)
    assert new_price == 0.00
    assert not validate_margin(margin)
    assert validate_currency(new_price)

def test_ProfMar_009_currency_exceed_max():
    wac = 500_000.00
    margin = 100
    new_price = calculate_new_price(wac, margin)
    assert new_price == 1_000_000.00
    assert not validate_currency(new_price)

def test_ProfMar_010_currency_exact_max():
    wac = 499_999.995
    margin = 100
    new_price = calculate_new_price(wac, margin)
    new_price_rounded = round(new_price, 2)
    assert new_price_rounded == 999_999.99
    assert validate_currency(new_price_rounded)
    assert validate_margin(100)
