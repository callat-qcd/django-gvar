"""Module provides models which store GVars."""
from django.db import models

from django_gvar.fields import GVarField
from django_gvar.serializers import GVarJSONEncoder, GVarJSONDecoder


class ExampleTable(models.Model):
    """Example table which stores a GVar field."""

    a = GVarField(help_text="Test field for GVars")


class MixedJSONFieldTable(models.Model):
    """Example table which displays a possibility to export lsqfit objects."""

    json = models.JSONField(
        encoder=GVarJSONEncoder,
        decoder=GVarJSONDecoder,
        help_text="Mixed GVar JSON field table.",
    )
