# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-29 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhukkad', '0003_auto_20190629_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='is_served',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
