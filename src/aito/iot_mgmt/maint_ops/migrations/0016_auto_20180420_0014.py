# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_MaintOps', '0015_auto_20180419_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='risk_score_name',
            field=models.CharField(max_length=255),
        ),
    ]
