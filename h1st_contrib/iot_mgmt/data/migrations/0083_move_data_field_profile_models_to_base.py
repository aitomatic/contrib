"""Move Data Field Profile models to Base module."""


# pylint: disable=invalid-name


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Move Data Field Profile models to Base module."""

    dependencies = [
        ('IoT_DataMgmt', '0082_auto_20200916_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentUniqueTypeGroupDataFieldProfile',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),

                ('to_date',
                 models.DateField(
                     blank=True,
                     db_index=True,
                     null=True)),

                ('valid_proportion',
                 models.FloatField()),

                ('n_distinct_values',
                 models.IntegerField()),

                ('distinct_values',
                 models.JSONField(
                     blank=True,
                     null=True)),

                ('sample_min',
                 models.FloatField(
                     blank=True,
                     null=True)),

                ('outlier_rst_min',
                 models.FloatField(
                     blank=True,
                     null=True)),

                ('sample_quartile',
                 models.FloatField(
                     blank=True,
                     null=True)),

                ('sample_median',
                 models.FloatField(
                     blank=True,
                     null=True)),

                ('sample_3rd_quartile',
                 models.FloatField(
                     blank=True,
                     null=True)),

                ('outlier_rst_max',
                 models.FloatField(
                     blank=True,
                     null=True)),

                ('sample_max',
                 models.FloatField(
                     blank=True,
                     null=True)),

                ('last_updated',
                 models.DateTimeField(
                     auto_now=True)),

                ('equipment_data_field',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.PROTECT,
                     related_name=('equipment_unique_type_group_'
                                   'data_field_profiles'),
                     related_query_name=('equipment_unique_type_group_'
                                         'data_field_profile'),
                     to='IoT_DataMgmt.equipmentdatafield')),

                ('equipment_unique_type_group',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.PROTECT,
                     related_name=('equipment_unique_type_group_'
                                   'data_field_profiles'),
                     related_query_name=('equipment_unique_type_group_'
                                         'data_field_profile'),
                     to='IoT_DataMgmt.equipmentuniquetypegroup'))
            ],

            options={
                'ordering': ('equipment_unique_type_group',
                             'equipment_data_field',
                             '-to_date'),

                'unique_together': {
                    ('equipment_unique_type_group',
                     'equipment_data_field',
                     'to_date')
                }
            }
        ),

        migrations.CreateModel(
            name='EquipmentUniqueTypeGroupDataFieldPairwiseCorrelation',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),

                ('sample_correlation',
                 models.FloatField()),

                ('last_updated',
                 models.DateTimeField(
                     auto_now=True)),

                ('equipment_data_field',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.PROTECT,
                     related_name=('equipment_unique_type_group_'
                                   'data_field_pairwise_correlations'),
                     related_query_name=('equipment_unique_type_group_'
                                         'data_field_pairwise_correlation'),
                     to='IoT_DataMgmt.equipmentdatafield')),

                ('equipment_data_field_2',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.PROTECT,
                     to='IoT_DataMgmt.equipmentdatafield')),

                ('equipment_unique_type_group',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.PROTECT,
                     related_name=('equipment_unique_type_group_'
                                   'data_field_pairwise_correlations'),
                     related_query_name=('equipment_unique_type_group_'
                                         'data_field_pairwise_correlation'),
                     to='IoT_DataMgmt.equipmentuniquetypegroup'))
            ],

            options={
                'ordering': ('equipment_unique_type_group',
                             'equipment_data_field',
                             'equipment_data_field_2'),

                'unique_together': {
                    ('equipment_unique_type_group',
                     'equipment_data_field',
                     'equipment_data_field_2')
                }
            }
        )
    ]
