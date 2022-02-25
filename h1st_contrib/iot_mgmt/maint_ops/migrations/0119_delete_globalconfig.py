"""Delete GlobalConfig model."""


# pylint: disable=invalid-name


from django.db import migrations


class Migration(migrations.Migration):
    """Delete GlobalConfig model."""

    dependencies = [
        ('IoT_MaintOps', '0118_EquipmentInstanceDailyPredictedFault')
    ]

    operations = [
        migrations.DeleteModel(
            name='GlobalConfig')
    ]
