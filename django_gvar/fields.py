"""Provides GVar field."""
from typing import Union

from django.db.models.fields import Field
from django.utils.translation import gettext_lazy as _

from gvar._gvarcore import GVar
from gvar import gdumps, gloads

from django_gvar.utils import parse_gvar


class GVarField(Field):
    """Field which stores gvars as TextFields.

    The database storage type are JSONFields.
    Internally, this class uses `gvar.gdumps` to store and `gvar.gloads` to load in data.
    """

    description = _("GVar")

    def get_internal_type(self) -> str:
        """Returns internal storage type (JSON)."""
        return "JSONField"

    def to_python(self, value: Union[GVar, None, str]) -> GVar:
        """Deserialzes object to GVar.

        Logic for deserialization:
        1. return if already a GVar
        2. return if None
        3. try `gloads` if string
        4. try `django_gvar.utils.parse_gvar` if gloads raises a TypeError
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
        """Dumps data to JSON using `gdumps`."""
        return gdumps(value)

    def value_to_string(self, obj: GVar) -> str:
        """Serializes object by calling `get_prep_value`."""
        value = self.value_from_object(obj)
        return self.get_prep_value(value)

    @staticmethod
    def from_db_value(value: str, expression, connection):
        """Inverse of `get_prep_value()`.

        Called when loaded from the db.
        See https://stackoverflow.com/q/48008026
        """
        if value is None:
            return value
        return gloads(value)
