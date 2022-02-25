"""H1st IoT Data Management: serializers."""


from rest_framework.serializers import (ModelSerializer,
                                        RelatedField,
                                        SlugRelatedField)

from drf_writable_nested.serializers import WritableNestedModelSerializer

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
)

from h1st_iot.util import clean_lower_str


class DataTypeSerializer(ModelSerializer):
    """DataTypeSerializer."""

    class Meta:
        """Metadata."""

        model = LogicalDataType

        fields = ('name',)


class NumericMeasurementUnitSerializer(ModelSerializer):
    """NumericMeasurementUnitSerializer."""

    class Meta:
        """Metadata."""

        model = NumericMeasurementUnit

        fields = ('name',)


class EquipmentDataFieldTypeSerializer(ModelSerializer):
    """EquipmentDataFieldTypeSerializer."""

    class Meta:
        """Metadata."""

        model = EquipmentDataFieldType

        fields = ('name',)


class EquipmentGeneralTypeSerializer(ModelSerializer):
    """EquipmentGeneralTypeSerializer."""

    class Meta:
        """Metadata."""

        model = EquipmentGeneralType

        fields = ('name',)


class EquipmentDataFieldRelatedField(RelatedField):
    """EquipmentDataFieldRelatedField."""

    def to_internal_value(self, data):
        """Get internal value."""
        return EquipmentDataField.objects.update_or_create(
            equipment_general_type=(
                EquipmentGeneralType.objects
                .get_or_create(
                    name=clean_lower_str(data['equipment_general_type']))[0]),
            name=clean_lower_str(data['name']),
            defaults=dict(
                equipment_data_field_type=(
                    EquipmentDataFieldType.objects
                    .get(name=clean_lower_str(
                        data['equipment_data_field_type']))),
                logical_data_type=(
                    LogicalDataType.objects
                    .get(name=clean_lower_str(data['logical_data_type']))),
                numeric_measurement_unit=(
                    NumericMeasurementUnit.objects
                    .get_or_create(
                        name=data['numeric_measurement_unit'].strip())[0]),
                lower_numeric_null=data['lower_numeric_null'],
                upper_numeric_null=data['upper_numeric_null'],
                min_val=data['min_val'],
                max_val=data['max_val']))[0]

    def to_representation(self, value):
        """Get representation."""
        return dict(
            id=value.id,
            equipment_general_type=value.equipment_general_type.name,
            name=value.name,
            description=value.description,
            equipment_data_field_type=value.equipment_data_field_type.name,
            logical_data_type=(value.logical_data_type.name
                               if value.logical_data_type
                               else None),
            numeric_measurement_unit=(value.numeric_measurement_unit.name
                                      if value.numeric_measurement_unit
                                      else None),
            lower_numeric_null=value.lower_numeric_null,
            upper_numeric_null=value.upper_numeric_null,
            min_val=value.min_val,
            max_val=value.max_val)


class EquipmentUniqueTypeRelatedField(RelatedField):
    """EquipmentUniqueTypeRelatedField."""

    def to_internal_value(self, data):
        """Get internal value."""
        return EquipmentUniqueType.objects.update_or_create(
            equipment_general_type=(
                EquipmentGeneralType.objects
                .get_or_create(
                    name=clean_lower_str(data['equipment_general_type']))[0]),
            name=clean_lower_str(data['name']))[0]

    def to_representation(self, value):
        """Get representation."""
        return dict(
            equipment_general_type=value.equipment_general_type.name,
            name=value.name)


class EquipmentUniqueTypeGroupRelatedField(RelatedField):
    """EquipmentUniqueTypeGroupRelatedField."""

    def to_internal_value(self, data):
        """Get internal value."""
        return EquipmentUniqueTypeGroup.objects.update_or_create(
            equipment_general_type=(
                EquipmentGeneralType.objects
                .get_or_create(
                    name=clean_lower_str(data['equipment_general_type']))[0]),
            name=clean_lower_str(data['name']))[0]

    def to_representation(self, value):
        """Get representation."""
        return dict(
            equipment_general_type=value.equipment_general_type.name,
            name=value.name)


class EquipmentDataFieldSerializer(WritableNestedModelSerializer):
    """EquipmentDataFieldSerializer."""

    equipment_general_type = \
        SlugRelatedField(
            queryset=EquipmentGeneralType.objects.all(), read_only=False,
            slug_field='name',
            many=False,
            required=True)

    equipment_data_field_type = \
        SlugRelatedField(
            queryset=EquipmentDataFieldType.objects.all(), read_only=False,
            slug_field='name',
            many=False,
            required=True)

    data_type = \
        SlugRelatedField(
            queryset=LogicalDataType.objects.all(), read_only=False,
            slug_field='name',
            many=False,
            required=False)

    numeric_measurement_unit = \
        SlugRelatedField(
            queryset=NumericMeasurementUnit.objects.all(), read_only=False,
            slug_field='name',
            many=False,
            required=False)

    equipment_unique_types = \
        EquipmentUniqueTypeRelatedField(
            queryset=EquipmentUniqueType.objects.all(), read_only=False,
            many=True,
            required=False)

    class Meta:
        """Metadata."""

        model = EquipmentDataField

        fields = (
            'id',
            'equipment_general_type',
            'name',
            'equipment_data_field_type',
            'logical_data_type',
            'numeric_measurement_unit',
            'lower_numeric_null',
            'upper_numeric_null',
            'min_val',
            'max_val',
            'equipment_unique_types',
        )


class EquipmentUniqueTypeGroupSerializer(WritableNestedModelSerializer):
    """EquipmentUniqueTypeGroupSerializer."""

    equipment_general_type = \
        SlugRelatedField(
            queryset=EquipmentGeneralType.objects.all(), read_only=False,
            slug_field='name',
            many=False,
            required=True)

    equipment_unique_types = \
        EquipmentUniqueTypeRelatedField(
            queryset=EquipmentUniqueType.objects.all(), read_only=False,
            many=True,
            required=False)

    equipment_data_fields = \
        EquipmentDataFieldRelatedField(
            queryset=EquipmentDataField.objects.all(), read_only=False,
            many=True,
            required=False)

    class Meta:
        """Metadata."""

        model = EquipmentUniqueTypeGroup

        fields = (
            'equipment_general_type',
            'name',
            'equipment_unique_types',
            'equipment_data_fields',
        )


class EquipmentUniqueTypeSerializer(WritableNestedModelSerializer):
    """EquipmentUniqueTypeSerializer."""

    equipment_general_type = \
        SlugRelatedField(
            queryset=EquipmentGeneralType.objects.all(), read_only=False,
            slug_field='name',
            many=False,
            required=True)

    equipment_data_fields = \
        EquipmentDataFieldRelatedField(
            queryset=EquipmentDataField.objects.all(), read_only=False,
            many=True,
            required=False)

    equipment_unique_type_groups = \
        EquipmentUniqueTypeGroupRelatedField(
            queryset=EquipmentUniqueTypeGroup.objects.all(), read_only=False,
            many=True,
            required=False)

    class Meta:
        """Metadata."""

        model = EquipmentUniqueType

        fields = (
            'equipment_general_type',
            'name',
            'equipment_data_fields',
            'equipment_unique_type_groups',
        )


class EquipmentFacilitySerializer(ModelSerializer):
    """EquipmentFacilitySerializer."""

    equipment_instances = \
        SlugRelatedField(
            queryset=EquipmentInstance.objects.all(), read_only=False,
            slug_field='name',
            many=True,
            required=False)

    class Meta:
        """Metadata."""

        model = EquipmentFacility

        fields = (
            'name',
            'info',
            'equipment_instances',
        )


class EquipmentInstanceSerializer(WritableNestedModelSerializer):
    """EquipmentInstanceSerializer."""

    equipment_general_type = \
        SlugRelatedField(
            queryset=EquipmentGeneralType.objects.all(), read_only=False,
            slug_field='name',
            many=False,
            required=True)

    equipment_unique_type = \
        EquipmentUniqueTypeRelatedField(
            queryset=EquipmentUniqueType.objects.all(), read_only=False,
            many=False,
            required=False)

    equipment_facility = \
        SlugRelatedField(
            queryset=EquipmentFacility.objects.all(), read_only=False,
            slug_field='name',
            many=False,
            required=False)

    equipment_unique_type_groups = \
        EquipmentUniqueTypeGroupRelatedField(
            queryset=EquipmentUniqueTypeGroup.objects.all(), read_only=False,
            many=True,
            required=False)

    class Meta:
        """Metadata."""

        model = EquipmentInstance

        fields = (
            'equipment_general_type',
            'equipment_unique_type',
            'equipment_facility',
            'name',
            'info',
            'equipment_unique_type_groups',
        )


class EquipmentSystemSerializer(ModelSerializer):
    """EquipmentSystemSerializer."""

    equipment_facility = \
        SlugRelatedField(
            queryset=EquipmentFacility.objects.all(), read_only=False,
            slug_field='name',
            many=False,
            required=False)

    equipment_instances = \
        SlugRelatedField(
            queryset=EquipmentInstance.objects.all(), read_only=False,
            slug_field='name',
            many=True,
            required=False)

    class Meta:
        """Metadata."""

        model = EquipmentSystem

        fields = (
            'id',
            'equipment_facility',
            'name',
            'date',
            'equipment_instances',
        )
