# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-12 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_MaintOps', '0023_auto_20180711_2246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipmentinstanceproblemdiagnosis',
            options={'ordering': ('-from_date', '-to_date', 'equipment_instance', 'dismissed')},
        ),
        migrations.AddField(
            model_name='equipmentinstanceproblemdiagnosis',
            name='dismissed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='equipmentinstanceproblemdiagnosis',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]