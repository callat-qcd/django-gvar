"""Tests for GVar field."""
from django.test import TestCase

from gvar import gvar, BufferDict

from django_gvar.fields import GVarField
from django_gvar.testing import assert_allclose

from field_tests.models import ExampleTable

__all___ = ["GvarFieldTestCase"]


class GvarFieldIOTestCase(TestCase):
    """Tests for the gvar field associated with read and write of actual GVars."""

    def test_gvar_dump_load_scalar(self):
        """Dumps gvar to db, reads it off and checks if gvars are equal."""
        a = gvar(1, 2)
        ExampleTable(a=a).save()
        a_stored = ExampleTable.objects.first().a
        assert_allclose(a, a_stored)

    def test_gvar_dump_load_array(self):
        """Dumps gvar to db, reads it off and checks if gvars are equal."""
        a = gvar([1, 2, 3], [[4, 5, 6], [5, 8, 7], [6, 7, 9]])
        ExampleTable(a=a).save()
        a_stored = ExampleTable.objects.first().a
        assert_allclose(a, a_stored)

    def test_gvar_dump_load_dict(self):
        """Dumps gvar to db, reads it off and checks if gvars are equal."""
        a1 = gvar(1, 2)
        a2 = gvar(2, 3)
        a = {"a1": a1, "a2": a2, "a1/a2": a1 / a2}
        ExampleTable(a=a).save()
        a_stored = ExampleTable.objects.first().a
        assert_allclose(a, a_stored)

    def test_gvar_dump_load_buffer_dict(self):
        """Dumps gvar to db, reads it off and checks if gvars are equal."""
        a1 = gvar(1, 2)
        a2 = gvar(2, 3)
        a = BufferDict(**{"a1": a1, "a2": a2, "a1/a2": a1 / a2})
        ExampleTable(a=a).save()
        a_stored = ExampleTable.objects.first().a
        assert_allclose(a, a_stored)


class GvarFieldFunctionalityTestCase(TestCase):
    """Tests for the gvar field associated with read and write of actual GVars."""

    def setUp(self):
        """Sets up empty and filled (saved) test etntries."""
        self.field = GVarField()

    # db field functionality tests
    def test_0_get_prep_value_empty(self):
        """Tests empty/null get prep values."""
        obj = None
        self.assertIs(self.field.get_prep_value(obj), obj)

    def test_0_from_db_value_empty(self):
        """Tests empty/null from prep values."""
        obj = None
        self.assertIs(self.field.from_db_value(obj, None, None), obj)

    def test_0_from_db_value_not_parsable(self):
        """Tests empty/null from prep values."""
        obj = "bad string"
        self.assertIs(self.field.from_db_value(obj, None, None), obj)

        obj = "1.0 2.0"
        self.assertIs(self.field.from_db_value(obj, None, None), obj)
