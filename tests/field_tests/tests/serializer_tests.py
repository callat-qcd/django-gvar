"""Tests for mixed JSON GVar fields."""
from numpy import array, ndarray
from numpy.testing import assert_allclose as assert_array_close

from django.test import TestCase

from gvar import gvar

from django_gvar.testing import assert_allclose

from field_tests.models import MixedJSONFieldTable


class GvarFieldIOTestCase(TestCase):
    """Tests for the gvar field associated with read and write of actual GVars."""

    def assert_dict_equal(self, d1, d2):
        self.assertIsInstance(d1, dict)
        self.assertIsInstance(d2, dict)
        self.assertEqual(d1.keys(), d2.keys())

        for key, v1 in d1.items():
            v2 = d2[key]
            self.assertEqual(type(v2), type(v1))
            if isinstance(v1, dict):
                self.assert_dict_equal(v1, v2)
            elif isinstance(v1, ndarray):
                assert_array_close(v1, v2)
            else:
                self.assertEqual(v1, v2)

    def test_01_dump_load_array(self):
        """Dumps gvar to db, reads it off and checks if gvars are equal."""
        json = array([1, 2, 3])
        MixedJSONFieldTable(json=json).save()
        json_stored = MixedJSONFieldTable.objects.first().json
        self.assertIsInstance(json_stored, ndarray)
        assert_array_close(json, json_stored)

    def test_02_dump_load_mixed_array(self):
        """Dumps gvar to db, reads it off and checks if gvars are equal."""
        json = {"a": array([1, 2, 3]), "b": 1}
        MixedJSONFieldTable(json=json).save()
        json_stored = MixedJSONFieldTable.objects.first().json
        self.assert_dict_equal(json_stored, json)

    def test_03_dump_load_nested_mixed_array(self):
        """Dumps gvar to db, reads it off and checks if gvars are equal."""
        json = {"a": {"c": array([1, 2, 3]), "d": 1}, "b": 1}
        MixedJSONFieldTable(json=json).save()
        json_stored = MixedJSONFieldTable.objects.first().json
        self.assert_dict_equal(json_stored, json)
