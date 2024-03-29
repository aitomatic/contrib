# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-14 00:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_MaintOps', '0051_equipmentinstancedailyriskscore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentinstancedailyriskscore',
            name='equipment_general_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='equipment_instance_daily_risk_scores', related_query_name='equipment_instance_daily_risk_score', to='IoT_DataMgmt.EquipmentGeneralType'),
        ),
        migrations.AlterField(
            model_name='equipmentinstancedailyriskscore',
            name='equipment_instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='equipment_instance_daily_risk_scores', related_query_name='equipment_instance_daily_risk_score', to='IoT_DataMgmt.EquipmentInstance'),
        ),
        migrations.AlterField(
            model_name='equipmentinstancedailyriskscore',
            name='equipment_unique_type_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='equipment_instance_daily_risk_scores', related_query_name='equipment_instance_daily_risk_score', to='IoT_DataMgmt.EquipmentUniqueTypeGroup'),
        ),
        migrations.AlterField(
            model_name='equipmentinstancedailyriskscore',
            name='risk_score_name',
            field=models.CharField(max_length=255),
        ),
    ]
