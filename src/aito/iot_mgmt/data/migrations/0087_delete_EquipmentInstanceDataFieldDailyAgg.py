"""Delete model EquipmentInstanceDataFieldDailyAgg."""


# pylint: disable=invalid-name


from django.db import migrations


class Migration(migrations.Migration):
    """Delete model EquipmentInstanceDataFieldDailyAgg."""

    dependencies = [
        ('IoT_DataMgmt', '0086_remove_last_updated_fields')
    ]

    operations = [
        migrations.DeleteModel(
            name='EquipmentInstanceDataFieldDailyAgg')
    ]
