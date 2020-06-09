"""Tests for GVar parsers."""
from pytest import raises

from gvar import gvar

from django_gvar.parser import parse_str_to_gvar, parse_gvar_to_str
from django_gvar.testing import assert_allclose

__all___ = ["*"]


def test_0_s2g_scalar_paranthesis():
    """Checks if `1(2)` is converted correctly."""
    expr = "1(2)"
    expected = gvar(1, 2)
    parsed = parse_str_to_gvar(expr)
    assert_allclose(expected, parsed)


def test_0_s2g_vector_paranthesis():
    """Checks if `1(2), 2(3), 3(4)` is converted correctly."""
    expr = "1(2), 2(3), 3(4)"
    expected = gvar([1, 2, 3], [2, 3, 4])
    parsed = parse_str_to_gvar(expr)
    assert_allclose(expected, parsed)


def test_0_s2g_vector_array():
    """Checks if `[1, 2, 3] | [4, 5, 6]` is converted correctly."""
    expr = "[1, 2, 3] | [4, 5, 6]"
    expected = gvar([1, 2, 3], [4, 5, 6])
    parsed = parse_str_to_gvar(expr)
    assert_allclose(expected, parsed)


def test_0_s2g_cov_array():
    """Checks if `[1, 3, 3] | [[4, 5, 6], [5, 7, 8], ...]` is converted correctly."""
    expr = "[1, 2, 3] | [[4, 5, 6], [5, 7, 8], [6, 8, 9]]"
    expected = gvar([1, 2, 3], [[4, 5, 6], [5, 7, 8], [6, 8, 9]])
    parsed = parse_str_to_gvar(expr)
    assert_allclose(expected, parsed)


def test_1_g2s_s2g_scalar():
    """Converts scalar gvar to string and back to gvar."""
    expected = gvar(1, 2)
    converted = parse_str_to_gvar(parse_gvar_to_str(expected))
    assert_allclose(expected, converted)


def test_1_g2s_s2g_vector_no_cov():
    """Converts vector gvar without correlation to string and back to gvar."""
    expected = gvar([1, 2, 3], [4, 5, 6])
    converted = parse_str_to_gvar(parse_gvar_to_str(expected))
    assert_allclose(expected, converted)


def test_1_g2s_s2g_vector_cov():
    """Converts vector gvar with correlation to string and back to gvar."""
    expected = gvar([1, 2, 3], [[4, 5, 6], [5, 7, 8], [6, 8, 9]])
    converted = parse_str_to_gvar(parse_gvar_to_str(expected))
    assert_allclose(expected, converted)


def test_2_g2s_miscv():
    """Tests gvar to string conversion in non-gvar cases."""
    obj = None
    assert parse_gvar_to_str(obj) == ""

    obj = "test string"
    assert parse_gvar_to_str(obj) == obj

    obj = 1.0
    with raises(TypeError):
        parse_gvar_to_str(obj)
