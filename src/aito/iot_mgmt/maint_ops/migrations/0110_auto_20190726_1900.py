# Generated by Django 2.2.3 on 2019-07-26 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_MaintOps', '0109_auto_20190528_1751'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipmentuniquetypegroupmonitoreddatafieldconfig',
            options={'ordering': ('-active', 'monitored_equipment_data_field__name')},
        ),
    ]
