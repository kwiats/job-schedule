from apps.earnings.models import Earnings, JobHours
from apps.users.models import Profile
from django.contrib import admin


class ProfileInLine(admin.TabularInline):  # type: ignore
    model = Profile


@admin.register(Earnings)
class EarningsAdmin(admin.ModelAdmin):  # type: ignore
    list_display = [
        "user",
        "age",
        "brutto_salary",
        "netto_salary",
    ]
    readonly_fields = [
        "age",
        "brutto_salary",
        "netto_salary",
        "pension_contribution",
        "disability_contribution",
        "sickness_contribution",
        "ZUS_contributions",
        "health_care_contribution",
        "income",
        "income_tax",
    ]

    fieldsets = (
        (
            "Profile informations",
            {
                "fields": (
                    "user",
                    "age",
                )
            },
        ),
        (
            "Salary informations",
            {
                "classes": (
                    "wide",
                    "extrapretty",
                ),
                "fields": (
                    (
                        "brutto_salary",
                        "netto_salary",
                    ),
                ),
            },
        ),
        (
            "Constants for calculations",
            {
                "classes": ("wide",),
                "fields": (
                    "constant_pension_contribution",
                    "constant_disability_contribution",
                    "constant_sickness_contribution",
                    "constant_health_care_contribution",
                    "constant_PIT",
                ),
            },
        ),
        (
            "Earnings informations",
            {
                "classes": (
                    "wide",
                    "extrapretty",
                ),
                "fields": (
                    (
                        "pension_contribution",
                        "disability_contribution",
                        "sickness_contribution",
                    ),
                    ("ZUS_contributions",),
                    "health_care_contribution",
                    (
                        "income",
                        "income_tax",
                    ),
                ),
            },
        ),
    )
    add_fieldsets = ()


@admin.register(JobHours)
class JobAdmin(admin.ModelAdmin):  # type: ignore
    list_display = [
        "user",
        "start_date",
        "end_date",
        "hours",
        "extra_hours",
    ]

    readonly_fields = [
        "hours",
        "extra_hours",
    ]
    fieldsets = (
        (
            "Profile informations",
            {
                "fields": (
                    "user",
                    "hours",
                    "extra_hours",
                )
            },
        ),
        (
            "Find hours between dates..",
            {
                "classes": (
                    "wide",
                    "extrapretty",
                ),
                "fields": (
                    (
                        "start_date",
                        "end_date",
                    ),
                ),
            },
        ),
    )
