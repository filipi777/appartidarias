# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-19 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0004_auto_20160817_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='number',
            field=models.IntegerField(default=1, verbose_name='numero'),
            preserve_default=False,
        ),
    ]
