# Generated by Django 4.1 on 2024-03-16 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "coach_appointment_system",
            "0002_rename_coaching_appointment_coach_appointment_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="coach_appointment",
            options={"verbose_name_plural": "Coach Appointment"},
        ),
        migrations.AlterModelOptions(
            name="coach_schedule", options={"verbose_name_plural": "Coach Schedule"},
        ),
    ]
