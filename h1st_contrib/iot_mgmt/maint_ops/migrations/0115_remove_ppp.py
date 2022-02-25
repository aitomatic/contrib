"""Remove PPP."""


# pylint: disable=invalid-name


from django.db import migrations


class Migration(migrations.Migration):
    """Remove PPP."""

    dependencies = [
        ('IoT_MaintOps', '0114_remove_last_updated_fields')
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name=('equipmentuniquetypegroupdatafield'
                  'blueprintbenchmarkmetricprofile'),
            unique_together=None),

        migrations.RemoveField(
            model_name=('equipmentuniquetypegroupdatafield'
                        'blueprintbenchmarkmetricprofile'),
            name='equipment_data_field'),

        migrations.RemoveField(
            model_name=('equipmentuniquetypegroupdatafield'
                        'blueprintbenchmarkmetricprofile'),
            name='equipment_unique_type_group'),

        migrations.AlterUniqueTogether(
            name='equipmentuniquetypegroupmonitoreddatafieldconfig',
            unique_together=None),

        migrations.RemoveField(
            model_name='equipmentuniquetypegroupmonitoreddatafieldconfig',
            name='equipment_unique_type_group_service_config'),

        migrations.RemoveField(
            model_name='equipmentuniquetypegroupmonitoreddatafieldconfig',
            name='manually_excluded_equipment_data_fields'),

        migrations.RemoveField(
            model_name='equipmentuniquetypegroupmonitoreddatafieldconfig',
            name='manually_included_equipment_data_fields'),

        migrations.RemoveField(
            model_name='equipmentuniquetypegroupmonitoreddatafieldconfig',
            name='monitored_equipment_data_field'),

        migrations.RemoveField(
            model_name='equipmentuniquetypegroupserviceconfig',
            name='equipment_unique_type_group'),

        migrations.RemoveField(
            model_name='equipmentuniquetypegroupserviceconfig',
            name='global_excluded_equipment_data_fields'),

        migrations.DeleteModel(
            name='Blueprint'),

        migrations.DeleteModel(
            name=('EquipmentUniqueTypeGroupDataField'
                  'BlueprintBenchmarkMetricProfile')),

        migrations.DeleteModel(
            name='EquipmentUniqueTypeGroupMonitoredDataFieldConfig'),

        migrations.DeleteModel(
            name='EquipmentUniqueTypeGroupServiceConfig')
    ]
