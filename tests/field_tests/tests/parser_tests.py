"""Tests for GVar parsers."""
from gvar import gvar

from django_gvar.parser import parse_str_to_gvar
from django_gvar.testing import assert_allclose

__all___ = ["*"]


def test_01_scalar_paranthesis():
    """Checks if `1(2)` is converted correctly."""
    expr = "1(2)"
    expected = gvar(1, 2)
    parsed = parse_str_to_gvar(expr)
    assert_allclose(expected, parsed)


def test_02_vector_paranthesis():
    """Checks if `1(2), 2(3), 3(4)` is converted correctly."""
    expr = "1(2), 2(3), 3(4)"
    expected = gvar([1, 2, 3], [2, 3, 4])
    parsed = parse_str_to_gvar(expr)
    assert_allclose(expected, parsed)


def test_03_vector_array():
    """Checks if `[1, 2, 3] | [4, 5, 6]` is converted correctly."""
    expr = "[1, 2, 3] | [4, 5, 6]"
    expected = gvar([1, 2, 3], [4, 5, 6])
    parsed = parse_str_to_gvar(expr)
    assert_allclose(expected, parsed)


def test_04_cov_array():
    """Checks if `[1, 3, 3] | [[4, 5, 6], [5, 7, 8], ...]` is converted correctly."""
    expr = "[1, 2, 3] | [[4, 5, 6], [5, 7, 8], [6, 8, 9]]"
    expected = gvar([1, 2, 3], [[4, 5, 6], [5, 7, 8], [6, 8, 9]])
    parsed = parse_str_to_gvar(expr)
    assert_allclose(expected, parsed)
