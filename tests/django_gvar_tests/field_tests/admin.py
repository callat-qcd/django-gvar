from django.contrib import admin
from .models import TestTable


class TestTableAdmin(admin.ModelAdmin):
    pass


admin.site.register(TestTable, TestTableAdmin)
