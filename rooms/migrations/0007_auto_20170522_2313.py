# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20170522_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(upload_to='static/image_upload'),
        ),
    ]
