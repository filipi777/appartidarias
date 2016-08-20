# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-17 12:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={'verbose_name': 'candidato'},
        ),
        migrations.AlterModelOptions(
            name='politicalparty',
            options={'verbose_name': ('sigla', 'partido político', 'diretório nacional', 'diretório estadual', 'diretório municipal', 'observações'), 'verbose_name_plural': ('siglas', 'partidos políticos', 'diretórios nacionais', 'diretórios estaduais', 'diretórios municipais', 'observações')},
        ),
        migrations.AddField(
            model_name='politicalparty',
            name='directory_city',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='politicalparty',
            name='directory_national',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='politicalparty',
            name='directory_state',
            field=models.TextField(default=datetime.datetime(2016, 8, 17, 12, 46, 14, 407840, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='politicalparty',
            name='initials',
            field=models.CharField(default='eu', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='politicalparty',
            name='obs',
            field=models.TextField(default='obs'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='name',
            field=models.CharField(max_length=128, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='political_party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.PoliticalParty', verbose_name='partido'),
        ),
    ]
