import re
import pytest

def is_valid_product_number(prod_num: str):
    """Kiểm tra Product Number hợp lệ (10 chữ số)."""
    return bool(re.fullmatch(r"\d{10}", prod_num))

def test_invalid_length_short():
    assert not is_valid_product_number("123456789")

def test_invalid_length_long():
    assert not is_valid_product_number("12345678901")

def test_invalid_non_digits():
    assert not is_valid_product_number("12345a7890")

def test_empty_input():
    assert not is_valid_product_number("")

def test_valid_10_digits():
    assert is_valid_product_number("1234567890")

def test_valid_leading_zeros():
    assert is_valid_product_number("0000000001")

def test_invalid_special_chars():
    assert not is_valid_product_number("123-456-78")
