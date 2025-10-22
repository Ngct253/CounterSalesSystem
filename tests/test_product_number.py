import re
import pytest

def is_valid_product_number(prod_num: str):
    """Kiểm tra Product Number hợp lệ (10 chữ số)."""
    return bool(re.fullmatch(r"\d{10}", prod_num))

# ===== INVALID TESTS =====
def test_ProdNum_001_invalid_length_short():
    assert not is_valid_product_number("123456789")  # <10 digits

def test_ProdNum_002_invalid_length_long():
    assert not is_valid_product_number("12345678901")  # >10 digits

def test_ProdNum_003_invalid_non_digits():
    assert not is_valid_product_number("12345a7890")  # contains letter

def test_ProdNum_010_empty_input():
    assert not is_valid_product_number("")  # empty

def test_ProdNum_009_invalid_special_chars():
    assert not is_valid_product_number("123-456-78")  # special chars

# ===== VALID TESTS =====
def test_ProdNum_004_valid_10_digits_non_existing():
    assert is_valid_product_number("0000000000")  # 10 digits, not in DB

def test_ProdNum_005_valid_existing_non_taxable():
    assert is_valid_product_number("1234567890")  # exists, non-taxable

def test_ProdNum_006_valid_existing_taxable():
    assert is_valid_product_number("0987654321")  # exists, taxable

def test_ProdNum_008_valid_leading_zeros_existing():
    assert is_valid_product_number("0000000001")  # leading zeros

def test_ProdNum_007_valid_max_digits_non_existing():
    assert is_valid_product_number("9999999999")  # boundary max digits
