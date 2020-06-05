"""Tests for GVar field."""
from django.test import TestCase

from gvar import gvar

from django_gvar.utils import parse_str_to_gvar
from django_gvar.testing import assert_allclose

from field_tests.models import ExampleTable


class GvarFieldTestCase(TestCase):
    """Tests for the gvar field."""

    def test_gvar_dump_load(self):
        """Dumps gvar to db, reads it off and checks if gvars are equal."""
        a = gvar([1, 2, 3], [[4, 5, 6], [5, 8, 7], [6, 7, 9]])

        ExampleTable(a=a).save()

        a_stored = ExampleTable.objects.first().a

        assert_allclose(a, a_stored)


class GVarParserTestCase(TestCase):
    """Checks if parser correctly converts strings to gvars."""

    def test_01_scalar_paranthesis(self):
        """Checks if `1(2)` is converted correctly."""
        expr = "1(2)"
        expected = gvar(1, 2)
        parsed = parse_str_to_gvar(expr)
        assert_allclose(expected, parsed)

    def test_02_vector_paranthesis(self):
        """Checks if `1(2), 2(3), 3(4)` is converted correctly."""
        expr = "1(2), 2(3), 3(4)"
        expected = gvar([1, 2, 3], [2, 3, 4])
        parsed = parse_str_to_gvar(expr)
        assert_allclose(expected, parsed)

    def test_03_vector_array(self):
        """Checks if `[1, 2, 3] | [4, 5, 6]` is converted correctly."""
        expr = "[1, 2, 3] | [4, 5, 6]"
        expected = gvar([1, 2, 3], [4, 5, 6])
        parsed = parse_str_to_gvar(expr)
        assert_allclose(expected, parsed)

    def test_04_cov_array(self):
        """Checks if `[1, 3, 3] | [[4, 5, 6], [5, 7, 8], ...]` is converted correctly."""
        expr = "[1, 2, 3] | [[4, 5, 6], [5, 7, 8], [6, 8, 9]]"
        expected = gvar([1, 2, 3], [[4, 5, 6], [5, 7, 8], [6, 8, 9]])
        parsed = parse_str_to_gvar(expr)
        assert_allclose(expected, parsed)
