from apps.earnings.models import Earnings
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
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("user"),
            },
        ),
    )
