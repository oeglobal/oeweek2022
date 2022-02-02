# Generated by Django 3.2.11 on 2022-01-23 19:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20220122_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='resource',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='institution_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='license',
            field=models.CharField(blank=True, choices=[('Public domain', 'Public domain'), ('CC-0', 'CC Zero (CC 0)'), ('CC-BY', 'CC Attribution (CC BY)'), ('CC-BY-SA', 'CC Attribution — Share-Alike (CC BY-SA)'), ('CC-BY-NC', 'CC Attribution — Non-Commercial (CC BY-NC)'), ('CC-NC-SA', 'CC Attribution — Non-Commercial — Share-Alike (CC BY-NC-SA)'), ('Other', 'Other open license')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='linkwebroom',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]