"""Remove last_updated fields."""


# pylint: disable=invalid-name


from django.db import migrations


class Migration(migrations.Migration):
    """Remove last_updated fields."""

    dependencies = [
        ('IoT_MaintOps',
         '0113_movel_data_field_profiles_to_base'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='last_updated'),

        migrations.RemoveField(
            model_name='blueprint',
            name='last_updated'),

        migrations.RemoveField(
            model_name='equipmentinstancealarmperiod',
            name='last_updated'),

        migrations.RemoveField(
            model_name='equipmentinstancedailyriskscore',
            name='last_updated'),

        migrations.RemoveField(
            model_name='equipmentinstanceproblemdiagnosis',
            name='last_updated'),

        migrations.RemoveField(
            model_name=('equipmentuniquetypegroupdatafield'
                        'blueprintbenchmarkmetricprofile'),
            name='last_updated'),

        migrations.RemoveField(
            model_name='equipmentuniquetypegroupserviceconfig',
            name='last_updated')
    ]
