# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-28 15:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0003_auto_20170527_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='prioridad',
            new_name='priority',
        ),
    ]
