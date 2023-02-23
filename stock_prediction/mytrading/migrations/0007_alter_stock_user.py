# Generated by Django 4.1.6 on 2023-02-23 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mytrading", "0006_stock"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
