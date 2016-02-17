# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20160208_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='notified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='resource',
            name='event_type',
            field=models.CharField(blank=True, choices=[('conference/forum/discussion', 'conference/forum/discussion'), ('webinar', 'webinar'), ('workshop', 'workshop'), ('local', 'local')], max_length=255),
        ),
    ]
