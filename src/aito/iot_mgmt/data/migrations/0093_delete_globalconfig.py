"""Delete GlobalConfig model."""


# pylint: disable=invalid-name


from django.db import migrations


class Migration(migrations.Migration):
    """Delete GlobalConfig model."""

    dependencies = [
        ('IoT_DataMgmt', '0092_verbose_names')
    ]

    operations = [
        migrations.DeleteModel(
            name='GlobalConfig')
    ]
