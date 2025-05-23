# Generated by Django 5.0.6 on 2024-07-27 18:11

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_alter_app_id_alter_displacedproduct_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="app",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("a61813d4-7719-4bc7-8b14-39f2d9a716cd"),
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="displacedproduct",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("7cd8097b-c774-43c1-883a-61d745c3a2e9"),
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("d1a9d438-6ab7-444f-a5d4-1a5e59e01c2e"),
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="ordersdeatails",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("05c43097-17c1-4115-a419-27de24517622"),
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("d0cf2c1b-96a0-4e60-9fce-a902d78dd5d2"),
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("86b7dc4a-f751-47eb-95af-a85c83bd1e29"),
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("22d1421f-ca91-4455-9103-ce5edeb4269b"),
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
