# Generated by Django 2.2.1 on 2019-05-11 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_DataMgmt', '0062_equipmentcomponent_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentcomponent',
            name='name',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Equipment Component'),
        ),
    ]