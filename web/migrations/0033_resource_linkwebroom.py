# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-02 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0032_auto_20170315_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='linkwebroom',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
