# Generated by Django 4.1.1 on 2022-10-08 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Med_assign",
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
                ("P_name", models.CharField(max_length=50)),
                ("d_name", models.CharField(max_length=50)),
                ("m_name", models.CharField(max_length=50)),
                ("desc", models.CharField(max_length=100)),
            ],
        ),
    ]