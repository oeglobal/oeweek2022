# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20160201_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]
