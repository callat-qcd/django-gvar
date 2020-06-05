"""Input converter for db field."""
from json import JSONDecodeError

from numpy import ndarray

from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES
from django.forms import Textarea
from django.forms.fields import CharField
from django.utils.translation import gettext_lazy as _

from gvar._gvarcore import GVar

from django_gvar.testing import assert_allclose
from django_gvar.utils import parse_str_to_gvar, parse_gvar_to_str


class EmptyValuesWrapper:
    """Wrapper which allows empty value checks on arrays.

    In the validation process of fields (from forms), Djagno checks if the value
    is in EMPTY_VALUES.
    But since GVars can be arrays, the check `value in list` potentially fails.
    This class wrapps the `in` operator such that elements of value are checked if
    value is an array.
    """

    empty_values = EMPTY_VALUES

    def __contains__(self, value):
        """Wrap contains to allow empty checks."""
        if isinstance(value, ndarray):
            out = any([val in self for val in value])
        else:
            out = value in self.empty_values

        return out


EMPTY_VALUES_WRAPPED = EmptyValuesWrapper()


class InvalidGVarInput(str):
    """Wrap input which is not convertable."""


class GVarField(CharField):
    """Class which parses input from string to gvar and vice versa."""

    default_error_messages = {
        "invalid": _("Enter a valid conversion string."),
    }
    widget = Textarea
    empty_values = EMPTY_VALUES_WRAPPED

    def to_python(self, value):
        """Tries to convert value to GVar."""
        if self.disabled:
            return value
        elif value in self.empty_values:
            return None
        elif isinstance(value, (GVar, ndarray)):
            return value

        try:
            return parse_str_to_gvar(value)
        except (JSONDecodeError, ValueError) as e:
            raise ValidationError(
                self.error_messages["invalid"],
                code="invalid",
                params={"value": value, "exception": e},
            )

    def bound_data(self, data, initial):
        if self.disabled:
            return initial
        try:
            return parse_str_to_gvar(data)
        except (JSONDecodeError, ValueError):
            return InvalidGVarInput(data)

    def prepare_value(self, value):
        if isinstance(value, InvalidGVarInput):
            return value
        return parse_gvar_to_str(value)

    def has_changed(self, initial, data):
        if self.disabled:
            return False
        return not assert_allclose(initial, self.to_python(data))
