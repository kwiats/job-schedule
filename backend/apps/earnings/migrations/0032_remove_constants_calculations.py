# Generated by Django 4.1.6 on 2023-02-07 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("earnings", "0031_constants_calculations_alter_calculations_constants"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="constants",
            name="calculations",
        ),
    ]