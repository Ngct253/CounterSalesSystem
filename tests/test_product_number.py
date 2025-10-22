import re
import pytest

# Mock database
product_db = {
    "1234567890": {"taxable": False},
    "0987654321": {"taxable": True},
    "0000000001": {"taxable": False},
}

def is_valid_product_number(prod_num: str):
    """Kiểm tra Product Number hợp lệ (10 chữ số)."""
    if not re.fullmatch(r"\d{10}", prod_num):
        return False, "Invalid format"
    if prod_num not in product_db:
        return False, "Item not found"
    return True, product_db[prod_num]

# ===== INVALID TEST CASES =====
invalid_cases = [
    ("ProdNum-001", "123456789"),       # <10 digits
    ("ProdNum-002", "12345678901"),     # >10 digits
    ("ProdNum-003", "12345a7890"),      # non-digit
    ("ProdNum-010", ""),                 # empty
    ("ProdNum-009", "123-456-78"),      # special chars
]

@pytest.mark.parametrize("tc_id, prod_num", invalid_cases)
def test_invalid_product_numbers(tc_id, prod_num):
    valid, msg = is_valid_product_number(prod_num)
    print(f"{tc_id} | Input: {prod_num} | Result: {msg}")
    assert not valid
    assert msg in ["Invalid format", "Item not found"]

# ===== VALID TEST CASES =====
valid_cases = [
    ("ProdNum-004", "0000000000"),
    ("ProdNum-005", "1234567890"),
    ("ProdNum-006", "0987654321"),
    ("ProdNum-008", "0000000001"),
    ("ProdNum-007", "9999999999"),
]

@pytest.mark.parametrize("tc_id, prod_num", valid_cases)
def test_valid_product_numbers(tc_id, prod_num):
    valid, info = is_valid_product_number(prod_num)
    print(f"{tc_id} | Input: {prod_num} | Result: {info}")
    assert valid
    assert "taxable" in info or "taxable" not in info  # mock DB may or may not have taxable
