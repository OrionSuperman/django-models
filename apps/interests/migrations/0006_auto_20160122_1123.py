# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0005_auto_20160122_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='created_at',
            field=models.DateTimeField(default=b'2016-01-22 UTC'),
        ),
    ]
