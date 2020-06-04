# Generated by Django 3.1a1 on 2020-06-04 14:31

from django.db import migrations, models
import django_gvar.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TestTable",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("a", django_gvar.fields.GVarField(help_text="This is a test")),
            ],
        ),
    ]
