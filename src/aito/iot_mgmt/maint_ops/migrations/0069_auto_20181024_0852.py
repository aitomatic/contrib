# Generated by Django 2.1.1 on 2018-10-24 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_MaintOps', '0068_auto_20181023_1636'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blueprint',
            options={'ordering': ('equipment_unique_type_group', '-trained_to_date', '-timestamp')},
        ),
        migrations.AlterModelOptions(
            name='equipmentinstancedailyriskscore',
            options={'ordering': ('equipment_unique_type_group', 'equipment_instance', 'risk_score_name', '-date')},
        ),
        migrations.AlterModelOptions(
            name='equipmentuniquetypegroupdatafieldblueprintbenchmarkmetricprofile',
            options={'ordering': ('equipment_unique_type_group', 'equipment_data_field', '-trained_to_date')},
        ),
        migrations.AlterModelOptions(
            name='equipmentuniquetypegroupdatafieldprofile',
            options={'ordering': ('equipment_unique_type_group', 'equipment_data_field', '-to_date')},
        ),
        migrations.AlterModelOptions(
            name='equipmentuniquetypegroupserviceconfig',
            options={'ordering': ('-active', 'equipment_unique_type_group')},
        ),
        migrations.RemoveField(
            model_name='alert',
            name='equipment_general_type',
        ),
        migrations.RemoveField(
            model_name='blueprint',
            name='equipment_general_type',
        ),
        migrations.RemoveField(
            model_name='equipmentinstancedailyriskscore',
            name='equipment_general_type',
        ),
        migrations.RemoveField(
            model_name='equipmentuniquetypegroupdatafieldblueprintbenchmarkmetricprofile',
            name='equipment_general_type',
        ),
        migrations.RemoveField(
            model_name='equipmentuniquetypegroupdatafieldprofile',
            name='equipment_general_type',
        ),
        migrations.RemoveField(
            model_name='equipmentuniquetypegroupserviceconfig',
            name='equipment_general_type',
        ),
    ]
