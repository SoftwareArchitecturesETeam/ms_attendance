# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-23 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20170923_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.PositiveSmallIntegerField(),
        ),
    ]