"""Verbose names."""


# pylint: disable=invalid-name


from django.db import migrations


class Migration(migrations.Migration):
    """Verbose names."""

    dependencies = [
        ('IoT_MaintOps', '0116_rename_alert_equipmentinstancealertperiod')
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alertdiagnosisstatus',
            options={'ordering': ('index',),
                     'verbose_name': 'Alert Diagnosis Status',
                     'verbose_name_plural': 'Alert Diagnosis Statuses'}),

        migrations.AlterModelOptions(
            name='equipmentinstancealarmperiod',
            options={'ordering': ('equipment_instance', '-from_utc_date_time'),
                     'verbose_name': 'Equipment Instance Alarm Period',
                     'verbose_name_plural': 'Equipment Instance Alarm Periods'}
        ),

        migrations.AlterModelOptions(
            name='equipmentinstancealertperiod',
            options={'ordering': ('diagnosis_status',
                                  '-ongoing',
                                  'risk_score_name',
                                  '-threshold',
                                  '-cumulative_excess_risk_score'),
                     'verbose_name': 'Equipment Instance Alert Period',
                     'verbose_name_plural': 'Equipment Instance Alert Periods'}
        ),

        migrations.AlterModelOptions(
            name='equipmentinstancedailyriskscore',
            options={
                'verbose_name': 'Equipment Instance Daily Risk Score',
                'verbose_name_plural': 'Equipment Instance Daily Risk Scores'
            }),

        migrations.AlterModelOptions(
            name='equipmentinstanceproblemdiagnosis',
            options={
                'ordering': ('dismissed', '-to_date', 'from_date'),
                'verbose_name': 'Equipment Instance Problem Diagnosis',
                'verbose_name_plural': 'Equipment Instance Problem Diagnoses'
            }),

        migrations.AlterModelOptions(
            name='equipmentproblemtype',
            options={'ordering': ('name',),
                     'verbose_name': 'Equipment Problem Type',
                     'verbose_name_plural': 'Equipment Problem Types'}),

        migrations.AlterModelOptions(
            name='globalconfig',
            options={'ordering': ('key',),
                     'verbose_name': 'Global Config',
                     'verbose_name_plural': 'Global Configs'})
    ]
