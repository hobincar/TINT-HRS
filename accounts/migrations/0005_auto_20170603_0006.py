# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170530_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='coupons',
            field=models.ManyToManyField(blank=True, to='memberships.Coupon'),
        ),
    ]