# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_auto_20160217_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]