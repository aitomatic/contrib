# Generated by Django 2.1.5 on 2019-02-23 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_DataMgmt', '0046_equipmentinstancedailymetadata_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentinstancedailymetadata',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
