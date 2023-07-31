"""Remove JSON Description fields to boost performance."""


# pylint: disable=invalid-name


from django.db import migrations


class Migration(migrations.Migration):
    """Remove JSON Description fields to boost performance."""

    dependencies = [
        ('IoT_DataMgmt', '0084_remove_EquipmentComponent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentdatafield',
            name='description'),

        migrations.RemoveField(
            model_name='equipmentuniquetype',
            name='description'),

        migrations.RemoveField(
            model_name='equipmentuniquetypegroup',
            name='description'),

        migrations.RemoveField(
            model_name='numericmeasurementunit',
            name='description'),
    ]
