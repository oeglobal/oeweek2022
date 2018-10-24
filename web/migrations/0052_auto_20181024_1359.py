# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-24 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0051_auto_20181024_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='event_other_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='event_type',
            field=models.CharField(blank=True, choices=[('conference/forum/discussion', 'Conference/forum/discussion'), ('conference/seminar', 'Conference/seminar'), ('workshop', 'Workshop'), ('forum/panel/discussion', 'Forum/panel/discussion'), ('other_local', 'other_local'), ('local', 'local'), ('webinar', 'Webinar'), ('discussion', 'Online Discussion'), ('other_online', 'Other - Online'), ('online', 'Online Event')], max_length=255, null=True),
        ),
    ]
