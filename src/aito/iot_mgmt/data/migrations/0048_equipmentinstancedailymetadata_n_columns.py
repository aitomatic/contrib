# Generated by Django 2.1.5 on 2019-02-23 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_DataMgmt', '0047_equipmentinstancedailymetadata_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentinstancedailymetadata',
            name='n_columns',
            field=models.IntegerField(default=0),
        ),
    ]
