# Generated by Django 2.1.5 on 2019-01-28 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_DataMgmt', '0036_auto_20190126_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentdatafield',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipmentdatafield',
            name='foreign_lang_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
