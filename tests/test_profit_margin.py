import pytest

# Tính New Price
def calc_new_price(wac, margin_percent):
    return round(wac * (1 + margin_percent / 100), 2)

# Kiểm tra hợp lệ theo business rule
def validate_margin(new_price, wac):
    profit_percent = ((new_price - wac) / wac) * 100
    if new_price < 0:
        return False, "Price below $0"
    if profit_percent < 30:
        return False, "Must make at least 30% profit"
    if new_price > 999_999.99:
        return False, "Price exceeds max $999,999.99"
    return True, "OK"

profit_cases = [
    ("ProfMar-001", 30, 100, True, "OK"),
    ("ProfMar-002", 29.99, 100, False, "Must make at least 30% profit"),
    ("ProfMar-003", 30.01, 100, True, "OK"),
    ("ProfMar-004", 999999, 100, False, "Price exceeds max $999,999.99"),
    ("ProfMar-005", -50, 100, False, "Must make at least 30% profit"),
    ("ProfMar-006", 0, 100, False, "Must make at least 30% profit"),
    ("ProfMar-007-IN", 0, 100, False, "Must make at least 30% profit"),
    ("ProfMar-007-OFF-below", 29, 100, False, "Must make at least 30% profit"),
    ("ProfMar-007-ON", 30, 100, True, "OK"),
    ("ProfMar-007-OFF-above", 31, 100, True, "OK"),
    ("ProfMar-008", -100, 100, False, "Price below $0"),
    ("ProfMar-009", 100, 500000, False, "Price exceeds max $999,999.99"),
    ("ProfMar-010", 100, 499999.995, True, "OK")
]


@pytest.mark.parametrize("tc_id, margin, wac, expected_valid", profit_cases)
def test_profit_margin(tc_id, margin, wac, expected_valid):
    new_price = calc_new_price(wac, margin)
    valid, msg = validate_margin(new_price, wac)
    print(f"{tc_id} | Margin: {margin} | WAC: {wac} | New Price: {new_price} | Result: {msg}")
    assert valid == expected_valid
