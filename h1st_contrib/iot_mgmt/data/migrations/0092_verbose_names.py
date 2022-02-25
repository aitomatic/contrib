"""Verbose names."""


# pylint: disable=invalid-name


from django.db import migrations, models


class Migration(migrations.Migration):
    """Verbose names."""

    dependencies = [
        ('IoT_DataMgmt', '0091_rename_logical_data_type')
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipmentdatafield',
            options={'ordering': ('equipment_general_type', 'name'),
                     'verbose_name': 'Equipment Data Field',
                     'verbose_name_plural': 'Equipment Data Fields'}),

        migrations.AlterModelOptions(
            name='equipmentdatafieldtype',
            options={'ordering': ('name',),
                     'verbose_name': 'Equipment Data Field Type',
                     'verbose_name_plural': 'Equipment Data Field Types'}),

        migrations.AlterModelOptions(
            name='equipmentfacility',
            options={'ordering': ('name',),
                     'verbose_name': 'Equipment Facility',
                     'verbose_name_plural': 'Equipment Facilities'}),

        migrations.AlterModelOptions(
            name='equipmentgeneraltype',
            options={'ordering': ('name',),
                     'verbose_name': 'Equipment General Type',
                     'verbose_name_plural': 'Equipment General Types'}),

        migrations.AlterModelOptions(
            name='equipmentinstance',
            options={'ordering': ('equipment_general_type',
                                  'equipment_unique_type',
                                  'name'),
                     'verbose_name': 'Equipment Instance',
                     'verbose_name_plural': 'Equipment Instances'}),

        migrations.AlterModelOptions(
            name='equipmentsystem',
            options={'ordering': ('equipment_facility', 'name', 'date'),
                     'verbose_name': 'Equipment System',
                     'verbose_name_plural': 'Equipment Systems'}),

        migrations.AlterModelOptions(
            name='equipmentuniquetype',
            options={'ordering': ('equipment_general_type', 'name'),
                     'verbose_name': 'Equipment Unique Type',
                     'verbose_name_plural': 'Equipment Unique Types'}),

        migrations.AlterModelOptions(
            name='equipmentuniquetypegroup',
            options={'ordering': ('equipment_general_type', 'name'),
                     'verbose_name': 'Equipment Unique Type Group',
                     'verbose_name_plural': 'Equipment Unique Type Groups'}),

        migrations.AlterModelOptions(
            name='equipmentuniquetypegroupdatafieldprofile',
            options={
                'ordering': ('equipment_unique_type_group',
                             'equipment_data_field',
                             '-to_date'),
                'verbose_name':
                    'Equipment Unique Type Group Data Field Profile',
                'verbose_name_plural':
                    'Equipment Unique Type Group Data Field Profiles'}),

        migrations.AlterModelOptions(
            name='globalconfig',
            options={'ordering': ('key',),
                     'verbose_name': 'Global Config',
                     'verbose_name_plural': 'Global Configs'}),

        migrations.AlterModelOptions(
            name='logicaldatatype',
            options={'ordering': ('name',),
                     'verbose_name': 'Logical Data Type',
                     'verbose_name_plural': 'Logical Data Types'}),

        migrations.AlterModelOptions(
            name='numericmeasurementunit',
            options={'ordering': ('name',),
                     'verbose_name': 'Numeric Measurement Unit',
                     'verbose_name_plural': 'Numeric Measurement Units'}),

        migrations.AlterField(
            model_name='logicaldatatype',
            name='name',
            field=models.CharField(
                db_index=True,
                max_length=255,
                unique=True,
                verbose_name='Logical Data Type'))
    ]
