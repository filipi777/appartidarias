# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-22 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0018_auto_20160822_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='elected',
            field=models.BooleanField(default=False, verbose_name='Eleita antes de 2012?'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='reelection',
            field=models.BooleanField(default=False, verbose_name='Re-eleição?'),
        ),
    ]
