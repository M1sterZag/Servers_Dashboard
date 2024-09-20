# Generated by Django 5.1.1 on 2024-09-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Card",
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
                ("name", models.CharField(max_length=100)),
                ("is_online", models.BooleanField()),
                ("ip", models.CharField(max_length=50)),
                ("up_date_time", models.DateTimeField()),
            ],
        ),
    ]
