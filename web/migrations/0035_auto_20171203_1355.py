# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-03 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0034_auto_20171202_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='year',
            field=models.IntegerField(blank=True, default=2018, null=True),
        ),
    ]
