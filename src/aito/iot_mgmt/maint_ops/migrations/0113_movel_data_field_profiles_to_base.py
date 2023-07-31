"""Move Data Field Profile models to Base module."""


# pylint: disable=invalid-name


from django.db import migrations


class Migration(migrations.Migration):
    """Move Data Field Profile models to Base module."""

    dependencies = [
        ('IoT_MaintOps', '0112_auto_20200916_2306'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='equipmentuniquetypegroupdatafieldprofile',
            unique_together=None),

        migrations.RemoveField(
            model_name='equipmentuniquetypegroupdatafieldprofile',
            name='equipment_data_field'),

        migrations.RemoveField(
            model_name='equipmentuniquetypegroupdatafieldprofile',
            name='equipment_unique_type_group'),

        migrations.DeleteModel(
            name='EquipmentUniqueTypeGroupDataFieldPairwiseCorrelation'),

        migrations.DeleteModel(
            name='EquipmentUniqueTypeGroupDataFieldProfile')
    ]
