# Generated by Django 4.1.6 on 2023-02-23 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mytrading", "0005_delete_stock"),
    ]

    operations = [
        migrations.CreateModel(
            name="Stock",
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
                ("name", models.CharField(max_length=16)),
                ("ticker", models.CharField(max_length=12)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trader",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
