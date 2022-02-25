"""Remove Data Field correlation model."""


# pylint: disable=invalid-name


from django.db import migrations


class Migration(migrations.Migration):
    """Remove Data Field correlation model."""

    dependencies = [
        ('IoT_DataMgmt', '0089_rename_LogicalDataType')
    ]

    operations = [
        migrations.DeleteModel(
            name='EquipmentUniqueTypeGroupDataFieldPairwiseCorrelation')
    ]
