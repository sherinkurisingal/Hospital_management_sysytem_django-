# Generated by Django 4.1.1 on 2022-10-13 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("patients", "0001_initial"),
        ("doctor", "0002_med_assign"),
    ]

    operations = [
        migrations.AddField(
            model_name="med_assign",
            name="m_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="patients.patient",
            ),
        ),
    ]
