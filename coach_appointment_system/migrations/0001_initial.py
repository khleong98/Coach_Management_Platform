# Generated by Django 4.1 on 2024-03-15 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("master", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Coaching_Appointment",
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
                ("from_time", models.DateTimeField()),
                ("to_time", models.DateTimeField()),
                (
                    "coach",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="master.coach"
                    ),
                ),
                (
                    "day",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="master.day"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Coaching_Appointment",
                "db_table": "cas_coaching_appointment",
            },
        ),
        migrations.CreateModel(
            name="Coach_Schedule",
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
                ("from_time", models.TimeField()),
                ("to_time", models.TimeField()),
                (
                    "coach",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="master.coach"
                    ),
                ),
                (
                    "day",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="master.day"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Coach_Schedule",
                "db_table": "cas_coach_schedule",
            },
        ),
    ]
