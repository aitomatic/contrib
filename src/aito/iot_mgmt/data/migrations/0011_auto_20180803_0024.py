# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-03 07:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_DataMgmt', '0010_auto_20180803_0015'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EquipmentInstanceAssociation',
            new_name='EquipmentEnsemble',
        ),
    ]
