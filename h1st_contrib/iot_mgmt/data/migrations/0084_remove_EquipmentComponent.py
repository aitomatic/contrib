"""Remove EquipmentComponent."""


# pylint: disable=invalid-name


from django.db import migrations


class Migration(migrations.Migration):
    """Remove EquipmentComponent."""

    dependencies = [
        ('IoT_DataMgmt',
         '0083_move_data_field_profile_models_to_base')
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentdatafield',
            name='equipment_components'),

        migrations.RemoveField(
            model_name='equipmentuniquetype',
            name='equipment_components'),

        migrations.RemoveField(
            model_name='equipmentuniquetypegroup',
            name='equipment_components'),

        migrations.DeleteModel(
            name='EquipmentComponent')
    ]
