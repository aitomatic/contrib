# Generated by Django 2.2.2 on 2019-06-26 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_DataMgmt', '0078_auto_20190626_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentcomponent',
            name='directly_interacts_with_components',
            field=models.ManyToManyField(blank=True, related_name='_equipmentcomponent_directly_interacts_with_components_+', related_query_name='equipment_component_directly_interacts_reverse', to='IoT_DataMgmt.EquipmentComponent'),
        ),
    ]