# Generated by Django 5.0.6 on 2024-08-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0017_product_shelf"),
    ]

    operations = [
        migrations.AddField(
            model_name="shelf",
            name="datetime",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
