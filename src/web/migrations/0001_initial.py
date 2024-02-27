# Generated by Django 5.0.2 on 2024-02-27 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attendee",
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
                ("name", models.CharField(max_length=200)),
                ("surname", models.CharField(default="", max_length=200, null=True)),
                ("birth_date", models.DateField(blank=True, null=True)),
                ("ticket_id", models.CharField(default="", max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Arrival",
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
                ("arrival", models.DateTimeField(blank=True, null=True)),
                ("departure", models.DateTimeField(blank=True, null=True)),
                ("added", models.DateTimeField(auto_now_add=True)),
                ("changed", models.DateTimeField(auto_now=True)),
                (
                    "ticket_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.attendee"
                    ),
                ),
            ],
        ),
    ]