# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-14 18:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_MaintOps', '0055_auto_20180914_1033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='average_excess_risk_score',
            new_name='approx_average_risk_score',
        ),
    ]
