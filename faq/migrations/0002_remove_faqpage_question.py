# Generated by Django 3.2.16 on 2022-11-01 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("faq", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="faqpage",
            name="question",
        ),
    ]
