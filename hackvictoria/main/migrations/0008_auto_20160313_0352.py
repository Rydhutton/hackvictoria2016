# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160313_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='destination',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trip',
            name='origin',
            field=models.CharField(max_length=200),
        ),
    ]
