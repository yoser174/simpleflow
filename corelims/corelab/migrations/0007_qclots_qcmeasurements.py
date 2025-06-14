# Generated by Django 4.2.19 on 2025-06-07 04:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("corelab", "0006_alter_results_numeric_result_alter_results_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="QCLots",
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
                ("control_name", models.CharField(max_length=100)),
                ("supplier", models.CharField(blank=True, max_length=100, null=True)),
                ("activation_date", models.DateField(blank=True, null=True)),
                ("deactivation_date", models.DateField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("review_status", models.BooleanField(default=False)),
                ("review_date", models.DateField(blank=True, null=True)),
                ("lot_number", models.CharField(max_length=100)),
                ("expiry_date", models.DateField(blank=True, null=True)),
                ("target_value", models.FloatField(blank=True, null=True)),
                ("standard_deviation", models.FloatField(blank=True, null=True)),
                ("control_range", models.FloatField(blank=True, null=True)),
                (
                    "instrument",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="qc_lots_instrument",
                        to="corelab.instruments",
                    ),
                ),
                (
                    "review_user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="qc_lots_review_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="qc_lots_test",
                        to="corelab.tests",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QCMeasurements",
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
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "qc_lot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="qc_lots_measurements",
                        to="corelab.qclots",
                    ),
                ),
                (
                    "result",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="qc_measurements",
                        to="corelab.instruments",
                    ),
                ),
            ],
        ),
    ]
