"""Registers the example table to the admin page."""

from django.contrib import admin
from field_tests.models import ExampleTable


@admin.register(ExampleTable)
class ExampleTableAdmin(admin.ModelAdmin):
    """Admin for the example table."""
