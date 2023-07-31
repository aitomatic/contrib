"""Remove last_updated fields."""


# pylint: disable=invalid-name


from django.db import migrations


class Migration(migrations.Migration):
    """Remove last_updated fields."""

    dependencies = [
        ('IoT_DataMgmt', '0085_remove_description_json_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentdatafield',
            name='last_updated'),

        migrations.RemoveField(
            model_name='equipmentfacility',
            name='last_updated'),

        migrations.RemoveField(
            model_name='equipmentinstance',
            name='last_updated'),

        migrations.RemoveField(
            model_name='equipmentinstancedatafielddailyagg',
            name='last_updated'),

        migrations.RemoveField(
            model_name='equipmentsystem',
            name='last_updated'),

        migrations.RemoveField(
            model_name='equipmentuniquetype',
            name='last_updated'),

        migrations.RemoveField(
            model_name='equipmentuniquetypegroup',
            name='last_updated'),

        migrations.RemoveField(
            model_name='equipmentuniquetypegroupdatafieldpairwisecorrelation',
            name='last_updated'),

        migrations.RemoveField(
            model_name='equipmentuniquetypegroupdatafieldprofile',
            name='last_updated')
    ]
