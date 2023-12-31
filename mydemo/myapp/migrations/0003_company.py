# Generated by Django 5.0 on 2023-12-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_post"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=50)),
                ("location", models.CharField(max_length=100)),
                ("about", models.TextField()),
                (
                    "type",
                    models.CharField(
                        choices=[("IT", "IT"), ("Non-IT", "Non-IT")], max_length=50
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("activity_status", models.BooleanField(default=True)),
            ],
        ),
    ]
