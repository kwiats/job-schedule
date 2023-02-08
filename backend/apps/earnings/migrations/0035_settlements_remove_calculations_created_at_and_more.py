# Generated by Django 4.1.6 on 2023-02-08 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("earnings", "0034_remove_salaries_calculations_calculations_salary_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Settlements",
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
                (
                    "created_at",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("date", models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="calculations",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="calculations",
            name="salary",
        ),
        migrations.RemoveField(
            model_name="calculations",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="calculations",
            name="user",
        ),
        migrations.RemoveField(
            model_name="constants",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="constants",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="jobhours",
            name="end_job",
        ),
        migrations.RemoveField(
            model_name="jobhours",
            name="start_job",
        ),
        migrations.AddField(
            model_name="calculations",
            name="hours",
            field=models.OneToOneField(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="earnings.jobhours",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="jobhours",
            name="end_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="jobhours",
            name="start_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name="Salaries",
        ),
        migrations.AddField(
            model_name="settlements",
            name="calculations",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="earnings.calculations"
            ),
        ),
        migrations.AddField(
            model_name="settlements",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
