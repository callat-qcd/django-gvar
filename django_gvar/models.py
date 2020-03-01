"""
"""
from typing import Union, Optional

from django import forms
from django.db.models.fields import Field
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from gvar._gvarcore import GVar  # pylint: disable=E0611
from gvar import dumps, loads  # pylint: disable=E0611


class GVarFormField(forms.Textarea):
    """
    """


class GVarField(Field):
    """Field which stores gvars as TextFields
    """

    description = _("GVar")

    def get_internal_type(self):
        return "TextField"

    def to_python(self, value: Union[GVar, None, str]) -> GVar:
        if isinstance(value, GVar):
            return value

        if value is None:
            return value

        return loads(value)

    def get_prep_value(self, value: GVar) -> str:
        return dumps(value)

    def value_to_string(self, obj: GVar) -> str:
        """Serialize object
        """
        value = self.value_from_object(obj)
        return self.get_prep_value(value)

    def from_db_value(self, value: str, expression, connection):
        """Inverse of get_prep_value().
        """
        if value is None:
            return value
        return loads(value)

    def formfield(self, **kwargs):
        # Passing max_length to forms.CharField means that the value's length
        # will be validated twice. This is considered acceptable since we want
        # the value in the form field (to pass into widget for example).
        return super().formfield(
            **{
                "max_length": self.max_length,
                **({} if self.choices is not None else {"widget": GVarFormField}),
                **kwargs,
            }
        )
