"""Tests for GVar field."""
from django.test import TestCase

from gvar import gvar

from field_tests.forms import ExampleTable
from field_tests.forms import ExampleForm


class GVarFormFieldTestCase(TestCase):
    """Test case for the widget and corresponding forms of GVarFields."""

    def test_0_form_valid_scalar(self):
        """Tests if valid data is converted as expected."""
        form_data = {"a": "1 | 2"}
        form = ExampleForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_0_form_valid_array(self):
        """Tests if valid data is converted as expected."""
        form_data = {"a": "[1, 2] | [2, 3]"}
        form = ExampleForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_0_form_valid_save(self):
        """Tests if valid data is converted as expected."""
        form_data = {"a": "[1, 2] | [2, 3]"}
        form = ExampleForm(data=form_data)
        form.save()
        self.assertTrue(form.is_valid())

    def test_1_form_empty(self):
        """Tests if form realizes it's empty."""
        form_data = {"a": ""}
        form = ExampleForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_1_form_with_inital_gvars(self):
        """Tests if form realizes it's empty."""
        instance = ExampleTable(a=gvar(1, 2))
        instance.save()
        form_data = {"a": instance.a}
        form = ExampleForm(data=form_data, instance=instance)
        self.assertTrue(form.is_valid())

    def test_1_form_invalid(self):
        """Tests if invalid data raises proper exceptions."""
        form_data = {"a": "[1, 2] | [2]"}
        form = ExampleForm(data=form_data)
        self.assertFalse(form.is_valid())
