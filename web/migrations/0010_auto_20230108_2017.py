# Generated by Django 3.2.16 on 2023-01-08 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0009_auto_20221214_1609"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="resource",
            name="opentags",
        ),
        migrations.AddField(
            model_name="resource",
            name="opentags_old",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]