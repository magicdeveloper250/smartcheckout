# Generated by Django 5.0.6 on 2024-08-01 17:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_alter_app_id_alter_app_last_use_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="link",
        ),
    ]
