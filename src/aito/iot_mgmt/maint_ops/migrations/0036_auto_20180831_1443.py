# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-31 21:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_MaintOps', '0035_auto_20180831_1410'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipmentuniquetypegroupdatafieldblueprintbenchmarkmetricprofile',
            options={'ordering': ('equipment_general_type', 'equipment_unique_type_group', 'equipment_data_field', '-to_date')},
        ),
        migrations.AlterModelOptions(
            name='equipmentuniquetypegroupdatafieldprofile',
            options={'ordering': ('equipment_general_type', 'equipment_unique_type_group', 'equipment_data_field', '-to_date')},
        ),
    ]
