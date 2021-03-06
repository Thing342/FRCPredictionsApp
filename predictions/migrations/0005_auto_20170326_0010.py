# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('predictions', '0004_load_initial_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'matches'},
        ),
        migrations.AlterField(
            model_name='event',
            name='district',
            field=models.CharField(
                choices=[('0', 'No District'), ('fim', 'Michigan'), ('mar', 'Mid-Atlantic'), ('ne', 'New England'),
                         ('pnw', 'Pacifc Northwest'), ('in', 'Indiana'), ('chs', 'Chesapeake'),
                         ('nc', 'North Carolina'), ('pch', 'Georgia'), ('ont', 'Ontario'), ('isr', 'Israel')],
                max_length=3, null=True, verbose_name='District'),
        ),
        migrations.AlterField(
            model_name='match',
            name='kpa',
            field=models.NullBooleanField(default=None, verbose_name='40 KPA Reached?'),
        ),
        migrations.AlterField(
            model_name='match',
            name='rotor',
            field=models.NullBooleanField(default=None, verbose_name='4 Rotors Active?'),
        ),
    ]
