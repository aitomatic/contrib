"""EquipmentInstanceDailyPredictedFault."""


# pylint: disable=invalid-name


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """EquipmentInstanceDailyPredictedFault."""

    dependencies = [
        ('IoT_DataMgmt', '0092_verbose_names'),
        ('IoT_MaintOps', '0117_verbose_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentInstanceDailyPredictedFault',

            fields=[
                ('id',
                 models.BigAutoField(
                     primary_key=True,
                     serialize=False)),

                ('equipment_unique_type_group',
                 models.ForeignKey(
                     help_text='Equipment Unique Type Group',
                     on_delete=django.db.models.deletion.PROTECT,
                     related_name='equipment_instance_daily_predicted_faults',
                     related_query_name=('equipment_instance_'
                                         'daily_predicted_fault'),
                     to='IoT_DataMgmt.equipmentuniquetypegroup',
                     verbose_name='Equipment Unique Type Group')),

                ('equipment_instance',
                 models.ForeignKey(
                     help_text='Equipment Instance',
                     on_delete=django.db.models.deletion.PROTECT,
                     related_name='equipment_instance_daily_predicted_faults',
                     related_query_name=('equipment_instance_'
                                         'daily_predicted_fault'),
                     to='IoT_DataMgmt.equipmentinstance',
                     verbose_name='Equipment Instance')),

                ('date',
                 models.DateField(
                     db_index=True,
                     help_text='Date',
                     verbose_name='Date')),

                ('fault_type',
                 models.ForeignKey(
                     help_text='Fault Type',
                     on_delete=django.db.models.deletion.PROTECT,
                     related_name='equipment_instance_daily_predicted_faults',
                     related_query_name=('equipment_instance_'
                                         'daily_predicted_fault'),
                     to='IoT_MaintOps.equipmentproblemtype',
                     verbose_name='Fault Type')),

                ('fault_predictor_name',
                 models.CharField(
                     db_index=True,
                     help_text='Fault Predictor Name',
                     max_length=255,
                     verbose_name='Fault Predictor Name')),

                ('predicted_fault_probability',
                 models.FloatField(
                     help_text='Predicted Fault Probability',
                     verbose_name='Predicted Fault Probability'))
            ],

            options={
                'verbose_name': 'Equipment Instance Daily Predicted Fault',
                'verbose_name_plural':
                    'Equipment Instance Daily Predicted Faults'
            }
        ),

        migrations.AddConstraint(
            model_name='equipmentinstancedailypredictedfault',
            constraint=models.UniqueConstraint(
                fields=('equipment_unique_type_group',
                        'equipment_instance',
                        'date',
                        'fault_type',
                        'fault_predictor_name'),
                name='EquipmentInstanceDailyPredictedFault_unique_together'))
    ]
