# Generated by Django 4.1.6 on 2023-02-07 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("earnings", "0033_alter_calculations_constants"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="salaries",
            name="calculations",
        ),
        migrations.AddField(
            model_name="calculations",
            name="salary",
            field=models.OneToOneField(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="earnings.salaries",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="calculations",
            name="constants",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="earnings.constants"
            ),
        ),
        migrations.AlterField(
            model_name="calculations",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.DeleteModel(
            name="Settlements",
        ),
    ]
