# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-27 09:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def forwards(apps, schema_editor):
    from web.models import Resource, ResourceImage

    for resource in Resource.objects.all():
        if resource.image:
            resource_image = ResourceImage.objects.create(image=resource.image)
            resource.resource_image = resource_image
            resource.save()


class Migration(migrations.Migration):
    dependencies = [
        ('web', '0044_resourceimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='resource_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.ResourceImage'),
        ),
        migrations.RunPython(forwards, hints={'target_db': 'default'}),
    ]
