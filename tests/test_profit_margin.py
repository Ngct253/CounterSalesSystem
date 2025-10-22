import pytest

# Tính New Price
def calc_new_price(wac, margin_percent):
    return round(wac * (1 + margin_percent / 100), 2)

# Kiểm tra hợp lệ theo quy tắc kinh doanh
def validate_margin(new_price, wac):
    profit_percent = ((new_price - wac) / wac) * 100
    if profit_percent < 30:
        return False, "Must make at least 30% profit"
    if new_price < 0:
        return False, "Price below $0"
    if new_price > 999_999.99:
        return False, "Price exceeds max $999,999.99"
    return True, "OK"

# Các test case dựa trên bảng thực tế
profit_cases = [
    ("ProfMar-001", 30, 100),
    ("ProfMar-002", 29.99, 100),
    ("ProfMar-003", 30.01, 100),
    ("ProfMar-004", 999999, 100),
    ("ProfMar-005", -50, 100),
    ("ProfMar-006", 0, 100),
    # DAT ON/OFF/IN
    ("ProfMar-007-IN", 0, 100),
    ("ProfMar-007-OFF-below", 29, 100),
    ("ProfMar-007-ON", 30, 100),
    ("ProfMar-007-OFF-above", 31, 100),
    ("ProfMar-008", -100, 100),
    ("ProfMar-009", 100, 500000),
    ("ProfMar-010", 100, 499999.995)
]

@pytest.mark.parametrize("tc_id, margin, wac", profit_cases)
def test_profit_margin(tc_id, margin, wac):
    new_price = calc_new_price(wac, margin)
    valid, msg = validate_margin(new_price, wac)
    print(f"{tc_id} | Margin: {margin} | WAC: {wac} | New Price: {new_price} | Result: {msg}")
    
    # Tự xác định pass/fail dựa trên quy tắc
    if ((new_price - wac) / wac) * 100 < 30 or new_price < 0 or new_price > 999_999.99:
        assert not valid
    else:
        assert valid
