"""Provides GVar field."""
from typing import Optional

from json import JSONDecodeError

from django.core.exceptions import ValidationError
from django.db.models.fields.json import JSONField
from django.utils.translation import gettext_lazy as _

from gvar._gvarcore import GVar
from gvar import gdumps, gloads
from gvar import __version__ as gvar_version_imported

from django_gvar.forms import GVarFormField
from django_gvar.forms import EMPTY_VALUES_WRAPPED


class GVarField(JSONField):
    """Field which stores gvars as TextFields.

    The database storage type are JSONFields.
    Internally, this class uses `gvar.gdumps` to store and `gvar.gloads` to load in data.

    This class is follows Djangos JSONField:
    https://github.com/django/django/blob/926148ef019abcac3a9988c78734d9336d69f24e/django/db/models/fields/json.py#L16
    """

    description = _("GVar")
    empty_values = EMPTY_VALUES_WRAPPED

    def __init__(
        self,
        verbose_name=None,
        name=None,
        encoder=None,
        decoder=None,
        gvar_version: Optional[str] = None,
        **kwargs,
    ):
        """Overloads default JSONField field by providing gvar version."""
        self.gvar_version = gvar_version or gvar_version_imported
        super().__init__(verbose_name, name, encoder=encoder, decoder=decoder, **kwargs)

    def deconstruct(self):
        """Adds gvar version to deconstruction."""
        name, path, args, kwargs = super().deconstruct()
        kwargs["gvar_version"] = gvar_version_imported
        return name, path, args, kwargs

    def get_internal_type(self) -> str:
        """Returns internal storage type (JSON)."""
        return "JSONField"

    def get_prep_value(self, value: GVar) -> Optional[str]:
        """Dumps data to JSON using `gdumps`."""
        if value is None:
            return value
        return gdumps(value)

    def value_to_string(self, obj: GVar) -> str:
        """Serializes object by calling `get_prep_value`."""
        value = self.value_from_object(obj)
        return self.get_prep_value(value)

    def validate(self, value: GVar, model_instance):
        """Validates value by executing a dump."""
        super(JSONField, self).validate(value, model_instance)
        try:
            gdumps(value)
        except ValidationError as e:
            raise TypeError(
                self.error_messages["invalid"] + "\n" + str(e),
                code="invalid",
                params={"value": value, "error": e},
            )

    def from_db_value(self, value: str, expression, connection):
        """Inverse of `get_prep_value()`.

        Called when loaded from the db.
        See https://stackoverflow.com/q/48008026
        """
        if value is None:
            return value

        try:
            return gloads(value)
        except (JSONDecodeError, ValueError, TypeError):
            return value

    def formfield(self, **kwargs):
        """Change widget to text area."""
        defaults = {"form_class": GVarFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)
