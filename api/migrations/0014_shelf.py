# Generated by Django 5.0.6 on 2024-08-30 08:27

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0013_product_qr_code"),
    ]

    operations = [
        migrations.CreateModel(
            name="Shelf",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("status", models.CharField(default="closed", max_length=64)),
                ("category", models.CharField(blank=True, max_length=64)),
                (
                    "session",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
