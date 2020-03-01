from django.db import models

from django_gvar.models import GVarField

# Create your models here.


class TestTable(models.Model):
    a = GVarField(help_text="This is a test")
