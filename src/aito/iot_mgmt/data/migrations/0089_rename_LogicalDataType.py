"""Rename LogicalDataType."""


# pylint: disable=invalid-name


from django.db import migrations


class Migration(migrations.Migration):
    """Rename LogicalDataType."""

    dependencies = [
        ('IoT_DataMgmt', '0088_remove_EquipmentDataField_default_val')
    ]

    operations = [
        migrations.RenameModel(
            old_name='DataType',
            new_name='LogicalDataType')
    ]
