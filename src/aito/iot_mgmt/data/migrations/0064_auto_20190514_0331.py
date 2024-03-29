# Generated by Django 2.2.1 on 2019-05-14 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_DataMgmt', '0063_auto_20190511_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentcomponent',
            name='equipment_data_fields',
            field=models.ManyToManyField(blank=True, related_name='equipment_components_reverse', related_query_name='equipment_component', to='IoT_DataMgmt.EquipmentDataField'),
        ),
        migrations.AlterField(
            model_name='equipmentcomponent',
            name='equipment_unique_types',
            field=models.ManyToManyField(blank=True, related_name='equipment_components_reverse', related_query_name='equipment_component', to='IoT_DataMgmt.EquipmentUniqueType'),
        ),
        migrations.AlterField(
            model_name='equipmentdatafield',
            name='equipment_unique_types',
            field=models.ManyToManyField(blank=True, related_name='equipment_data_fields_reverse', related_query_name='equipment_data_field', to='IoT_DataMgmt.EquipmentUniqueType'),
        ),
        migrations.AlterField(
            model_name='equipmentuniquetypegroup',
            name='equipment_unique_types',
            field=models.ManyToManyField(blank=True, related_name='equipment_unique_type_groups_reverse', related_query_name='equipment_unique_type_group', to='IoT_DataMgmt.EquipmentUniqueType'),
        ),
    ]
