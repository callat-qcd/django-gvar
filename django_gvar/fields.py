"""
"""
from typing import Union

from django import forms
from django.db.models.fields import Field
from django.utils.translation import gettext_lazy as _

from gvar._gvarcore import GVar  # pylint: disable=E0611
from gvar import gdumps, gloads  # pylint: disable=E0611

from django_gvar.utils import parse_gvar


class GVarField(Field):
    """Field which stores gvars as TextFields
    """

    description = _("GVar")

    def get_internal_type(self):
        return "JSONField"

    def to_python(self, value: Union[GVar, None, str]) -> GVar:
        """Deserialze object
        """
        if isinstance(value, GVar):
            return value

        if value is None:
            return value

        if isinstance(value, str):
            try:
                return gloads(value)
            except TypeError:
                return parse_gvar(value)

    def get_prep_value(self, value: GVar) -> str:
        return gdumps(value)

    def value_to_string(self, obj: GVar) -> str:
        """Serialize object
        """
        value = self.value_from_object(obj)
        return self.get_prep_value(value)

    @staticmethod
    def from_db_value(value: str, expression, connection):  # pylint: disable=W0613
        """Inverse of get_prep_value(). Called when loaded from the db

        See https://stackoverflow.com/q/48008026
        """
        if value is None:
            return value
        return gloads(value)

    def formfield(self, **kwargs):
        # Passing max_length to forms.CharField means that the value's length
        # will be validated twice. This is considered acceptable since we want
        # the value in the form field (to pass into widget for example).
        return super().formfield(
            **{
                "max_length": self.max_length,
                **({} if self.choices is not None else {"widget": forms.Textarea}),
                **kwargs,
            }
        )
