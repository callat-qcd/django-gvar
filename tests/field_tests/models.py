"""Module provides models which store GVars."""
from django.db import models

from django_gvar.fields import GVarField


class ExampleTable(models.Model):
    """Example table which stores a GVar field."""

    a = GVarField(help_text="Test field for GVars")
