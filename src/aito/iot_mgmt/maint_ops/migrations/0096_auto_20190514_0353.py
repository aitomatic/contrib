# Generated by Django 2.2.1 on 2019-05-14 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_MaintOps', '0095_auto_20190514_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentinstancealarmperiod',
            name='equipment_instance_alert_periods',
            field=models.ManyToManyField(blank=True, related_name='equipment_instance_alarm_periods_reverse', related_query_name='equipment_instance_alarm_period', to='IoT_MaintOps.Alert'),
        ),
        migrations.AlterField(
            model_name='equipmentinstancealarmperiod',
            name='equipment_instance_problem_diagnoses',
            field=models.ManyToManyField(blank=True, related_name='equipment_instance_alarm_periods_reverse', related_query_name='equipment_instance_alarm_period', to='IoT_MaintOps.EquipmentInstanceProblemDiagnosis'),
        ),
        migrations.AlterField(
            model_name='equipmentinstanceproblemdiagnosis',
            name='alert_periods',
            field=models.ManyToManyField(blank=True, related_name='equipment_instance_problem_diagnoses_reverse', related_query_name='equipment_instance_problem_diagnosis', to='IoT_MaintOps.Alert'),
        ),
    ]
