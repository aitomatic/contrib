"""Rename Alert model."""


# pylint: disable=invalid-name


from django.db import migrations


class Migration(migrations.Migration):
    """Rename Alert model."""

    dependencies = [
        ('IoT_DataMgmt', '0089_rename_LogicalDataType'),
        ('IoT_MaintOps', '0115_remove_ppp')
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alert',
            new_name='EquipmentInstanceAlertPeriod')
    ]
