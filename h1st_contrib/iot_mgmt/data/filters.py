"""H1st IoT Data Management Filters."""


from django.db.models.fields.json import JSONField

from rest_framework_filters import CharFilter, FilterSet, RelatedFilter

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


class DataTypeFilter(FilterSet):
    """DataTypeFilter."""

    class Meta:
        """DataTypeFilter metadata."""

        model = LogicalDataType

        fields = dict(
            name=['exact']
        )


class NumericMeasurementUnitFilter(FilterSet):
    """NumericMeasurementUnitFilter."""

    class Meta:
        """NumericMeasurementUnitFilter metadata."""

        model = NumericMeasurementUnit

        fields = dict(
            name=[
                'exact', 'iexact',
                'in',
                'contains', 'icontains',
                'startswith', 'istartswith', 'endswith', 'iendswith',
                'regex', 'iregex'
            ]
        )


class EquipmentDataFieldTypeFilter(FilterSet):
    """EquipmentDataFieldTypeFilter."""

    class Meta:
        """EquipmentDataFieldTypeFilter metadata."""

        model = EquipmentDataFieldType

        fields = dict(
            name=['exact']
        )


class EquipmentGeneralTypeFilter(FilterSet):
    """EquipmentGeneralTypeFilter."""

    class Meta:
        """EquipmentGeneralTypeFilter metadata."""

        model = EquipmentGeneralType

        fields = dict(
            name=[
                'exact', 'iexact',
                'in',
                'contains', 'icontains',
                'startswith', 'istartswith', 'endswith', 'iendswith',
                'regex', 'iregex'
            ]
        )


class EquipmentDataFieldFilter(FilterSet):
    """EquipmentDataFieldFilter."""

    equipment_general_type = \
        RelatedFilter(
            queryset=EquipmentGeneralType.objects.all(),
            filterset=EquipmentGeneralTypeFilter)

    equipment_data_field_type = \
        RelatedFilter(
            queryset=EquipmentDataFieldType.objects.all(),
            filterset=EquipmentDataFieldTypeFilter)

    data_type = \
        RelatedFilter(
            queryset=LogicalDataType.objects.all(),
            filterset=DataTypeFilter)

    numeric_measurement_unit = \
        RelatedFilter(
            queryset=NumericMeasurementUnit.objects.all(),
            filterset=NumericMeasurementUnitFilter)

    equipment_unique_types = \
        RelatedFilter(
            queryset=EquipmentUniqueType.objects.all(),
            filterset='EquipmentUniqueTypeFilter')

    class Meta:
        """EquipmentDataFieldFilter metadata."""

        model = EquipmentDataField

        fields = dict(
            name=[
                'exact', 'iexact',
                'in',
                'contains', 'icontains',
                'startswith', 'istartswith', 'endswith', 'iendswith',
                'regex', 'iregex'
            ],

            lower_numeric_null=[
                'exact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',
                'startswith',
                'endswith',
                'range'
            ],

            upper_numeric_null=[
                'exact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',
                'startswith',
                'endswith',
                'range'
            ],

            min_val=[
                'exact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',
                'startswith',
                'endswith',
                'range',
                'isnull'
            ],

            max_val=[
                'exact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',
                'startswith',
                'endswith',
                'range',
                'isnull'
            ],

            description='__all__')

        filter_overrides = {
            JSONField: dict(
                filter_class=CharFilter
                # 'extra': lambda f: {'lookup_expr': 'icontains'}
            )
        }


class EquipmentUniqueTypeGroupFilter(FilterSet):
    """EquipmentUniqueTypeGroupFilter."""

    equipment_general_type = \
        RelatedFilter(
            queryset=EquipmentGeneralType.objects.all(),
            filterset=EquipmentGeneralTypeFilter)

    equipment_unique_types = \
        RelatedFilter(
            queryset=EquipmentUniqueType.objects.all(),
            filterset='EquipmentUniqueTypeFilter')

    equipment_data_fields = \
        RelatedFilter(
            queryset=EquipmentDataField.objects.all(),
            filterset=EquipmentDataFieldFilter)

    class Meta:
        """EquipmentUniqueTypeGroupFilter metadata."""

        model = EquipmentUniqueTypeGroup

        fields = dict(
            name=[
                'exact', 'iexact',
                'in',
                'contains', 'icontains',
                'startswith', 'istartswith', 'endswith', 'iendswith',
                'regex', 'iregex'
            ],

            description='__all__')

        filter_overrides = {
            JSONField: dict(
                filter_class=CharFilter
                # 'extra': lambda f: {'lookup_expr': 'icontains'}
            )
        }


class EquipmentUniqueTypeFilter(FilterSet):
    """EquipmentUniqueTypeFilter."""

    equipment_general_type = \
        RelatedFilter(
            queryset=EquipmentGeneralType.objects.all(),
            filterset=EquipmentGeneralTypeFilter)

    equipment_data_fields = \
        RelatedFilter(
            queryset=EquipmentDataField.objects.all(),
            filterset=EquipmentDataFieldFilter)

    equipment_unique_type_groups = \
        RelatedFilter(
            queryset=EquipmentUniqueTypeGroup.objects.all(),
            filterset=EquipmentUniqueTypeGroupFilter)

    class Meta:
        """EquipmentUniqueTypeFilter metadata."""

        model = EquipmentUniqueType

        fields = dict(
            name=[
                'exact', 'iexact',
                'in',
                'contains', 'icontains',
                'startswith', 'istartswith', 'endswith', 'iendswith',
                'regex', 'iregex'
            ],

            description='__all__')

        filter_overrides = {
            JSONField: dict(
                filter_class=CharFilter
                # 'extra': lambda f: {'lookup_expr': 'icontains'}
            )
        }


class EquipmentFacilityFilter(FilterSet):
    """EquipmentFacilityFilter."""

    class Meta:
        """EquipmentFacilityFilter metadata."""

        model = EquipmentFacility

        fields = dict(
            name=[
                'exact', 'iexact',
                'in',
                'contains', 'icontains',
                'startswith', 'istartswith', 'endswith', 'iendswith',
                'regex', 'iregex'
            ],

            info='__all__')

        filter_overrides = {
            JSONField: dict(
                filter_class=CharFilter
                # 'extra': lambda f: {'lookup_expr': 'icontains'}
            )
        }


class EquipmentInstanceFilter(FilterSet):
    """EquipmentInstanceFilter."""

    equipment_general_type = \
        RelatedFilter(
            queryset=EquipmentGeneralType.objects.all(),
            filterset=EquipmentGeneralTypeFilter)

    equipment_unique_type = \
        RelatedFilter(
            queryset=EquipmentUniqueType.objects.all(),
            filterset=EquipmentUniqueTypeFilter)

    equipment_facility = \
        RelatedFilter(
            queryset=EquipmentFacility.objects.all(),
            filterset=EquipmentFacilityFilter)

    class Meta:
        """EquipmentInstanceFilter metadata."""

        model = EquipmentInstance

        fields = dict(
            name=[
                'exact', 'iexact',
                'in',
                'contains', 'icontains',
                'startswith', 'istartswith', 'endswith', 'iendswith',
                'regex', 'iregex'
            ],

            info='__all__')

        filter_overrides = {
            JSONField: dict(
                filter_class=CharFilter
                # 'extra': lambda f: {'lookup_expr': 'icontains'}
            )
        }


class EquipmentSystemFilter(FilterSet):
    """EquipmentSystemFilter."""

    equipment_facility = \
        RelatedFilter(
            queryset=EquipmentFacility.objects.all(),
            filterset=EquipmentFacilityFilter)

    equipment_instances = \
        RelatedFilter(
            queryset=EquipmentInstance.objects.all(),
            filterset=EquipmentInstanceFilter)

    class Meta:
        """EquipmentSystemFilter metadata."""

        model = EquipmentSystem

        fields = dict(
            name=[
                'exact', 'iexact',
                'in',
                'contains', 'icontains',
                'startswith', 'istartswith', 'endswith', 'iendswith',
                'regex', 'iregex'
            ],

            date=[
                'exact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',
                'startswith',
                'endswith',
                'range',
                'isnull',
                'year',
                'year__gt', 'year__gte', 'year__lt', 'year__lte',
                'year__in',
                'year__range',
                'month',
                'month__gt', 'month__gte', 'month__lt', 'month__lte',
                'month__in',
                'month__range'
            ])
