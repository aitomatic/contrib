# Generated by Django 2.1.5 on 2019-01-30 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_DataMgmt', '0037_auto_20190128_2137'),
        ('IoT_MaintOps', '0078_auto_20190106_0247'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentUniqueTypeGroupDataFieldPairwiseCorrelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_date', models.DateField(blank=True, db_index=True, null=True)),
                ('sample_correlation', models.FloatField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('equipment_data_field', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='equipment_unique_type_group_data_field_pairwise_correlations', related_query_name='equipment_unique_type_group_data_field_pairwise_correlation', to='IoT_DataMgmt.EquipmentDataField')),
                ('equipment_data_field_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='IoT_DataMgmt.EquipmentDataField')),
                ('equipment_unique_type_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='equipment_unique_type_group_data_field_pairwise_correlations', related_query_name='equipment_unique_type_group_data_field_pairwise_correlation', to='IoT_DataMgmt.EquipmentUniqueTypeGroup')),
            ],
            options={
                'ordering': ('equipment_unique_type_group', '-to_date', '-sample_correlation'),
            },
        ),
    ]
