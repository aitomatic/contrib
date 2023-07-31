"""Rename logical_data_type field."""


# pylint: disable=invalid-name


from django.db import migrations


class Migration(migrations.Migration):
    """Rename logical_data_type field."""

    dependencies = [
        ('IoT_DataMgmt', '0090_remove_correlation')
    ]

    operations = [
        migrations.RenameField(
            model_name='equipmentdatafield',
            old_name='data_type',
            new_name='logical_data_type')
    ]
