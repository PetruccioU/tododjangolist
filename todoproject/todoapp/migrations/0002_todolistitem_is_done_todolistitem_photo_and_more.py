# Generated by Django 4.0.4 on 2023-01-25 16:53

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistitem',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todolistitem',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todolistitem',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='todolistitem',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todolistitem',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
