# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-01 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enterprise', '0018_auto_20170701_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='code',
            field=models.IntegerField(default=13200645),
        ),
    ]
