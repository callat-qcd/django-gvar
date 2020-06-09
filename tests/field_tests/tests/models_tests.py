"""Tests for GVar field."""
from django.test import TestCase

from gvar import gvar, BufferDict

from django_gvar.testing import assert_allclose

from field_tests.models import ExampleTable

__all___ = ["GvarFieldTestCase"]


class GvarFieldTestCase(TestCase):
    """Tests for the gvar field."""

    def test_01_gvar_dump_load_scalar(self):
        """Dumps gvar to db, reads it off and checks if gvars are equal."""
        a = gvar(1, 2)
        ExampleTable(a=a).save()
        a_stored = ExampleTable.objects.first().a
        assert_allclose(a, a_stored)

    def test_02_gvar_dump_load_array(self):
        """Dumps gvar to db, reads it off and checks if gvars are equal."""
        a = gvar([1, 2, 3], [[4, 5, 6], [5, 8, 7], [6, 7, 9]])
        ExampleTable(a=a).save()
        a_stored = ExampleTable.objects.first().a
        assert_allclose(a, a_stored)

    def test_03_gvar_dump_load_dict(self):
        """Dumps gvar to db, reads it off and checks if gvars are equal."""
        a1 = gvar(1, 2)
        a2 = gvar(2, 3)
        a = {"a1": a1, "a2": a2, "a1/a2": a1 / a2}
        ExampleTable(a=a).save()
        a_stored = ExampleTable.objects.first().a
        assert_allclose(a, a_stored)

    def test_04_gvar_dump_load_buffer_dict(self):
        """Dumps gvar to db, reads it off and checks if gvars are equal."""
        a1 = gvar(1, 2)
        a2 = gvar(2, 3)
        a = BufferDict(**{"a1": a1, "a2": a2, "a1/a2": a1 / a2})
        ExampleTable(a=a).save()
        a_stored = ExampleTable.objects.first().a
        assert_allclose(a, a_stored)
