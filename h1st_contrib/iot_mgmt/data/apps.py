"""H1st IoT Data Management Base module config."""


from django.apps.config import AppConfig


class H1stIoTDataManagementBaseModuleConfig(AppConfig):
    """H1st IoT Data Management Base module config."""

    name = 'h1st_contrib.iot_mgmt.data_mgmt'

    label = 'IoT_DataMgmt'

    verbose_name = 'H1st IoT Data Management'

    def ready(self):
        """Run scripts/tasks to initialize module."""
        # pylint: disable=import-outside-toplevel
        from h1st_contrib.iot_mgmt.data_mgmt.scripts import (
            create_logical_data_types,
            create_control_and_measurement_equipment_data_field_types,
        )

        create_logical_data_types.run()
        create_control_and_measurement_equipment_data_field_types.run()
