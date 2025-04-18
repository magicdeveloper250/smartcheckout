# Generated by Django 5.0.6 on 2024-07-27 17:43

import api.models
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("6b0c6f6f-c87d-4747-b3fb-50efa08cd415"),
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=128, null=True)),
                ("category", models.CharField(default="None", max_length=128)),
                ("quality", models.CharField(default="None", max_length=255)),
                ("unit", models.CharField(default="Number", max_length=64)),
                (
                    "unit_in_stock",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "unit_on_order",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "reorder_level",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("product_available", models.BooleanField(default=False)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("link", models.TextField(null=True)),
                ("description", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("b042279d-fbf0-4599-870f-a8a747bf639d"),
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=16)),
                (
                    "email",
                    models.EmailField(
                        blank=True, default="", max_length=254, unique=True
                    ),
                ),
                ("password", models.TextField(null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "date_joined",
                    models.DateTimeField(verbose_name=django.utils.timezone.now),
                ),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", api.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name="App",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("d1630342-3fe7-4b20-a38a-b2d178324063"),
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("status", models.CharField(default="Active", max_length=64)),
                ("last_use", models.DateTimeField(auto_now=True)),
                (
                    "cust_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("8a6c46df-799f-4765-9fc3-edda6573079e"),
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("time", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(default="Processing", max_length=64)),
                ("value", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "tax",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "cust_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrdersDeatails",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("7d34e3b7-1629-4113-a7ea-f07014d5cdd7"),
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("product_id", models.CharField(max_length=255)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("quantity", models.SmallIntegerField()),
                (
                    "total",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "tax",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "order_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.order"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("b856ad65-1667-471b-a81c-0d9687110ce4"),
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("channel", models.CharField(default="MTN MoMo", max_length=64)),
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "amount",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "cust_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "order_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="api.order"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DisplacedProduct",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("77fbe83d-06f6-4e9a-a160-4911b8c9236b"),
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "cust_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.product"
                    ),
                ),
            ],
        ),
    ]
