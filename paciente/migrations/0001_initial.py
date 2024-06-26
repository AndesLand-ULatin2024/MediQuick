# Generated by Django 5.0.6 on 2024-06-20 03:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Paciente",
            fields=[
                ("name", models.CharField(max_length=250)),
                ("lasName", models.CharField(max_length=250)),
                ("age", models.IntegerField()),
                (
                    "document",
                    models.PositiveBigIntegerField(
                        default=None,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("civilStatus", models.CharField(max_length=250)),
                ("country", models.CharField(max_length=250)),
                ("job", models.CharField(max_length=250)),
                ("address", models.TextField()),
            ],
        ),
    ]
