# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-25 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_MaintOps', '0058_auto_20180916_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='last_risk_score',
            field=models.FloatField(default=0),
        ),
    ]
