"""H1st IoT Data Management: querysets."""


from django.db.models import Prefetch

from h1st_iot.data_mgmt.models import (
    LogicalDataType,
    NumericMeasurementUnit,
    EquipmentDataFieldType,
    EquipmentGeneralType,
    EquipmentDataField,
    EquipmentUniqueTypeGroup,
    EquipmentUniqueType,
    EquipmentFacility,
    EquipmentInstance,
    EquipmentSystem,
    EquipmentUniqueTypeGroupDataFieldProfile,
)


DATA_TYPE_QUERYSET = \
    LogicalDataType.objects.all()


NUMERIC_MEASUREMENT_UNIT_NAME_ONLY_UNORDERED_QUERYSET = \
    NumericMeasurementUnit.objects \
    .only('name') \
    .order_by()


NUMERIC_MEASUREMENT_UNIT_QUERYSET = \
    NumericMeasurementUnit.objects.all()


EQUIPMENT_DATA_FIELD_TYPE_QUERYSET = \
    EquipmentDataFieldType.objects.all()


EQUIPMENT_GENERAL_TYPE_UNORDERED_QUERYSET = \
    EquipmentGeneralType.objects \
    .order_by()


EQUIPMENT_GENERAL_TYPE_QUERYSET = \
    EquipmentGeneralType.objects.all()


EQUIPMENT_DATA_FIELD_ID_ONLY_UNORDERED_QUERYSET = \
    EquipmentDataField.objects \
    .only('id') \
    .order_by()


EQUIPMENT_DATA_FIELD_NAME_ONLY_QUERYSET = \
    EquipmentDataField.objects \
    .only('name') \
    .order_by('name')


EQUIPMENT_DATA_FIELD_INCL_DESCRIPTION_QUERYSET = \
    EquipmentDataField.objects \
    .select_related(
        'equipment_general_type',
        'equipment_data_field_type',
        'logical_data_type',
        'numeric_measurement_unit')


EQUIPMENT_DATA_FIELD_STR_QUERYSET = \
    EQUIPMENT_DATA_FIELD_INCL_DESCRIPTION_QUERYSET


EQUIPMENT_DATA_FIELD_STR_UNORDERED_QUERYSET = \
    EQUIPMENT_DATA_FIELD_STR_QUERYSET \
    .order_by()


EQUIPMENT_UNIQUE_TYPE_GROUP_ID_ONLY_UNORDERED_QUERYSET = \
    EquipmentUniqueTypeGroup.objects \
    .only('id') \
    .order_by()


EQUIPMENT_UNIQUE_TYPE_GROUP_NAME_ONLY_QUERYSET = \
    EquipmentUniqueTypeGroup.objects \
    .only('name') \
    .order_by('name')


EQUIPMENT_UNIQUE_TYPE_GROUP_INCL_DESCRIPTION_QUERYSET = \
    EquipmentUniqueTypeGroup.objects \
    .select_related(
        'equipment_general_type')


EQUIPMENT_UNIQUE_TYPE_GROUP_STR_QUERYSET = \
    EQUIPMENT_UNIQUE_TYPE_GROUP_INCL_DESCRIPTION_QUERYSET


EQUIPMENT_UNIQUE_TYPE_GROUP_STR_UNORDERED_QUERYSET = \
    EQUIPMENT_UNIQUE_TYPE_GROUP_STR_QUERYSET \
    .order_by()


EQUIPMENT_UNIQUE_TYPE_ID_ONLY_UNORDERED_QUERYSET = \
    EquipmentUniqueType.objects \
    .only('id') \
    .order_by()


EQUIPMENT_UNIQUE_TYPE_NAME_ONLY_QUERYSET = \
    EquipmentUniqueType.objects \
    .defer(
        'equipment_general_type') \
    .order_by(
        'name')


EQUIPMENT_UNIQUE_TYPE_INCL_DESCRIPTION_QUERYSET = \
    EquipmentUniqueType.objects \
    .select_related(
        'equipment_general_type')


EQUIPMENT_UNIQUE_TYPE_STR_QUERYSET = \
    EQUIPMENT_UNIQUE_TYPE_INCL_DESCRIPTION_QUERYSET


EQUIPMENT_UNIQUE_TYPE_STR_UNORDERED_QUERYSET = \
    EQUIPMENT_UNIQUE_TYPE_STR_QUERYSET \
    .order_by()


EQUIPMENT_DATA_FIELD_REST_API_QUERYSET = \
    EQUIPMENT_DATA_FIELD_INCL_DESCRIPTION_QUERYSET \
    .prefetch_related(
        Prefetch(
            lookup='equipment_unique_types',
            queryset=EQUIPMENT_UNIQUE_TYPE_INCL_DESCRIPTION_QUERYSET))


EQUIPMENT_UNIQUE_TYPE_GROUP_REST_API_QUERYSET = \
    EQUIPMENT_UNIQUE_TYPE_GROUP_INCL_DESCRIPTION_QUERYSET \
    .prefetch_related(
        Prefetch(
            lookup='equipment_unique_types',
            queryset=EQUIPMENT_UNIQUE_TYPE_INCL_DESCRIPTION_QUERYSET),
        Prefetch(
            lookup='equipment_data_fields',
            queryset=EQUIPMENT_DATA_FIELD_INCL_DESCRIPTION_QUERYSET))


EQUIPMENT_UNIQUE_TYPE_REST_API_QUERYSET = \
    EQUIPMENT_UNIQUE_TYPE_INCL_DESCRIPTION_QUERYSET \
    .prefetch_related(
        Prefetch(
            lookup='equipment_data_fields',
            queryset=EQUIPMENT_DATA_FIELD_INCL_DESCRIPTION_QUERYSET),
        Prefetch(
            lookup='equipment_unique_type_groups',
            queryset=EQUIPMENT_UNIQUE_TYPE_GROUP_INCL_DESCRIPTION_QUERYSET))


EQUIPMENT_INSTANCE_ID_ONLY_UNORDERED_QUERYSET = \
    EquipmentInstance.objects \
    .only('id') \
    .order_by()


EQUIPMENT_INSTANCE_RELATED_TO_EQUIPMENT_UNIQUE_TYPE_ID_ONLY_UNORDERED_QUERYSET = (   # noqa: E501
    EquipmentInstance.objects
    .only('id', 'equipment_unique_type')
    .order_by())


EQUIPMENT_INSTANCE_RELATED_TO_EQUIPMENT_FACILITY_ID_ONLY_UNORDERED_QUERYSET = \
    EquipmentInstance.objects \
    .only(
        'id',
        'equipment_facility') \
    .order_by()


EQUIPMENT_INSTANCE_RELATED_TO_EQUIPMENT_FACILITY_STR_QUERYSET = \
    EquipmentInstance.objects \
    .only(
        'name',
        'equipment_facility') \
    .order_by(
        'name')


EQUIPMENT_INSTANCE_NAME_ONLY_QUERYSET = \
    EquipmentInstance.objects \
    .only(
        'name') \
    .order_by(
        'name')


EQUIPMENT_INSTANCE_STR_QUERYSET = \
    EquipmentInstance.objects \
    .defer(
        'equipment_facility',
        'info') \
    .select_related(
        'equipment_general_type',
        'equipment_unique_type') \
    .defer(
        'equipment_unique_type__equipment_general_type')


EQUIPMENT_INSTANCE_REST_API_QUERYSET = \
    EquipmentInstance.objects \
    .select_related(
        'equipment_general_type',
        'equipment_unique_type',
        'equipment_unique_type__equipment_general_type',
        'equipment_facility') \
    .defer(
        'equipment_facility__info') \
    .prefetch_related(
        Prefetch(
            lookup='equipment_unique_type_groups',
            queryset=EQUIPMENT_UNIQUE_TYPE_GROUP_INCL_DESCRIPTION_QUERYSET))


EQUIPMENT_FACILITY_NAME_ONLY_UNORDERED_QUERYSET = \
    EquipmentFacility.objects \
    .only('name') \
    .order_by()


EQUIPMENT_FACILITY_STR_QUERYSET = \
    EquipmentFacility.objects


EQUIPMENT_FACILITY_REST_API_QUERYSET = \
    EQUIPMENT_FACILITY_STR_QUERYSET \
    .prefetch_related(
        Prefetch(
            lookup='equipment_instances',
            queryset=EQUIPMENT_INSTANCE_RELATED_TO_EQUIPMENT_FACILITY_STR_QUERYSET))   # noqa: E501


EQUIPMENT_SYSTEM_REST_API_QUERYSET = \
    EquipmentSystem.objects \
    .select_related(
        'equipment_facility') \
    .defer(
        'equipment_facility__info') \
    .prefetch_related(
        Prefetch(
            lookup='equipment_instances',
            queryset=EQUIPMENT_INSTANCE_NAME_ONLY_QUERYSET))


EQUIPMENT_UNIQUE_TYPE_GROUP_DATA_FIELD_PROFILE_REST_API_QUERYSET = \
    EquipmentUniqueTypeGroupDataFieldProfile.objects \
    .select_related(
        'equipment_unique_type_group',
        'equipment_data_field',
        'equipment_data_field__equipment_general_type',
        'equipment_data_field__equipment_data_field_type',
        'equipment_data_field__data_type',
        'equipment_data_field__numeric_measurement_unit') \
    .defer(
        'equipment_unique_type_group__equipment_general_type')
