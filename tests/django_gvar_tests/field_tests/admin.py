from django.contrib import admin
from .models import TestTable


class TestTableAdmin(admin.ModelAdmin):
    list_display = ("id", "a")


admin.site.register(TestTable, TestTableAdmin)
