# Generated by Django 3.2.16 on 2023-01-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0011_emailqueueitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailqueueitem",
            name="priority",
            field=models.IntegerField(default=1),
        ),
    ]
