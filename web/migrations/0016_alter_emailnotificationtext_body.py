# Generated by Django 3.2.16 on 2023-01-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0015_auto_20230116_1910"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailnotificationtext",
            name="body",
            field=models.TextField(
                blank=True,
                help_text="You can use the following variables in body and title: {firstname}, {lastname}, {title}, {slug1}, {slug2}, {uuid} and {year}. HTML is not allowed.",
            ),
        ),
    ]
