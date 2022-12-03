# Generated by Django 3.2.16 on 2022-11-29 13:50

from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0007_alter_resource_year"),
    ]

    operations = [
        migrations.AddField(
            model_name="resource",
            name="user_image",
            field=models.ImageField(
                blank=True,
                upload_to=web.models.UploadToResourceImageDir("images/resource/"),
                validators=[web.models.validate_image],
            ),
        ),
    ]