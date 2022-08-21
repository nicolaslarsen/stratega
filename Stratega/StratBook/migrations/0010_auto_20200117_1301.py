# Generated by Django 3.0.1 on 2020-01-17 12:01

import StratBook.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StratBook', '0009_auto_20200115_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='nade',
            name='setup_img',
            field=models.ImageField(blank=True, null=True, upload_to=StratBook.models.nade_directory_path),
        ),
        migrations.AddField(
            model_name='nade',
            name='setup_img_link',
            field=models.URLField(blank=True),
        ),
    ]
