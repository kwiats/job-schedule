# Generated by Django 4.1.6 on 2023-02-04 12:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_profile_birth_date_alter_profile_salary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="salary",
            field=models.FloatField(
                default=0.0,
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=0, message="Salary cannot be less than 0"
                    ),
                    django.core.validators.MaxValueValidator(
                        limit_value=9999999999,
                        message="Sorry, but we need to have some limits ;)",
                    ),
                ],
                verbose_name="brutto salary",
            ),
        ),
    ]