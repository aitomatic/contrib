# Generated by Django 2.2.1 on 2019-05-16 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_DataMgmt', '0069_auto_20190514_1740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipmentfacility',
            options={'ordering': ('name',), 'verbose_name_plural': 'equipment_facilities'},
        ),
    ]
