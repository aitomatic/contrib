# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-03 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_DataMgmt', '0011_auto_20180803_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentfacility',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
