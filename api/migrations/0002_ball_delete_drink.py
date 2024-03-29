# Generated by Django 5.0.3 on 2024-03-05 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ball",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("position", models.JSONField()),
                ("velocity", models.JSONField()),
                ("speed", models.FloatField()),
                ("direction", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name="Drink",
        ),
    ]
