# Generated by Django 4.1 on 2024-03-16 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("master", "0002_alter_utc_offset"),
        ("coach_appointment_system", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Coaching_Appointment", new_name="Coach_Appointment",
        ),
        migrations.AlterModelOptions(
            name="coach_appointment",
            options={"verbose_name_plural": "Coach_Appointment"},
        ),
        migrations.AlterModelTable(
            name="coach_appointment", table="cas_coach_appointment",
        ),
    ]
