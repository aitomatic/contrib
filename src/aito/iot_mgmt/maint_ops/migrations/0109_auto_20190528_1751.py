# Generated by Django 2.2.1 on 2019-05-28 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_MaintOps', '0108_auto_20190523_0259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipmentinstanceproblemdiagnosis',
            options={'ordering': ('dismissed', '-to_date', 'from_date')},
        ),
        migrations.RemoveField(
            model_name='equipmentinstanceproblemdiagnosis',
            name='ongoing',
        ),
    ]
