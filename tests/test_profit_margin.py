import pytest

# Profit Margin calculation: New Price = WAC * (1 + Margin%)
def calc_new_price(wac, margin_percent):
    return round(wac * (1 + margin_percent/100), 2)

# Mock validation
def validate_margin(new_price, wac):
    profit_percent = ((new_price - wac) / wac) * 100
    if profit_percent < 30:
        return False, "Must make at least 30% profit"
    if new_price < 0:
        return False, "Price below $0"
    if new_price > 999_999.99:
        return False, "Price exceeds max $999,999.99"
    return True, "OK"

profit_cases = [
    ("ProfMar-001", 30, 100),       # min 30%
    ("ProfMar-002", 29.99, 100),    # invalid <30
    ("ProfMar-003", 30.01, 100),    # just above 30%
    ("ProfMar-004", 999999, 100),   # very high margin
    ("ProfMar-005", -50, 100),      # negative margin
    ("ProfMar-006", 0, 100),        # zero margin
    ("ProfMar-007", 0, 100),        # DAT IN/ON/OFF multiple checks
    ("ProfMar-008", -100, 100),     # currency min 0
    ("ProfMar-009", 100, 500000),   # exceed currency max
    ("ProfMar-010", 100, 499999.995) # exact max
]

@pytest.mark.parametrize("tc_id, margin, wac", profit_cases)
def test_profit_margin(tc_id, margin, wac):
    new_price = calc_new_price(wac, margin)
    valid, msg = validate_margin(new_price, wac)
    print(f"{tc_id} | Margin: {margin} | WAC: {wac} | New Price: {new_price} | Result: {msg}")
    # TC 002,005,006,008,009 expected invalid
    if tc_id in ["ProfMar-002", "ProfMar-005", "ProfMar-006", "ProfMar-008", "ProfMar-009", "ProfMar-004"]:
        assert not valid
    else:
        assert valid
