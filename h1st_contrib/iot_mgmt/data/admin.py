"""H1st IoT Data Management: admin."""


from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin, TabularInline
from django.db.models.query import Prefetch
from django.forms.models import BaseInlineFormSet

from silk.profiling.profiler import silk_profile

from h1st_iot.data_mgmt.models import (
    NumericMeasurementUnit,
    EquipmentGeneralType,
    EquipmentDataField,
    EquipmentUniqueTypeGroup,
    EquipmentUniqueType,
    EquipmentFacility,
    EquipmentInstance,
    EquipmentSystem,
    EquipmentUniqueTypeGroupDataFieldProfile,
)
from h1st_iot.data_mgmt.querysets import (
    EQUIPMENT_DATA_FIELD_ID_ONLY_UNORDERED_QUERYSET,
    EQUIPMENT_DATA_FIELD_STR_QUERYSET,
    EQUIPMENT_UNIQUE_TYPE_GROUP_ID_ONLY_UNORDERED_QUERYSET,
    EQUIPMENT_UNIQUE_TYPE_GROUP_NAME_ONLY_QUERYSET,
    EQUIPMENT_UNIQUE_TYPE_ID_ONLY_UNORDERED_QUERYSET,
    EQUIPMENT_UNIQUE_TYPE_NAME_ONLY_QUERYSET,
    EQUIPMENT_INSTANCE_ID_ONLY_UNORDERED_QUERYSET,
    EQUIPMENT_INSTANCE_RELATED_TO_EQUIPMENT_UNIQUE_TYPE_ID_ONLY_UNORDERED_QUERYSET,   # noqa: E501
    EQUIPMENT_INSTANCE_RELATED_TO_EQUIPMENT_FACILITY_ID_ONLY_UNORDERED_QUERYSET,   # noqa: E501
)


# pylint: disable=invalid-name,line-too-long


@register(NumericMeasurementUnit)
class NumericMeasurementUnitAdmin(ModelAdmin):
    """NumericMeasurementUnit admin."""

    list_display = ('name',)

    show_full_result_count = False

    @silk_profile(name='Admin: Numeric Measurement Units')
    def changelist_view(self, *args, **kwargs):
        """Change-list view."""
        return super().changelist_view(*args, **kwargs)

    @silk_profile(name='Admin: Numeric Measurement Unit')
    def changeform_view(self, *args, **kwargs):
        """Change-form view."""
        return super().changeform_view(*args, **kwargs)


@register(EquipmentGeneralType)
class EquipmentGeneralTypeAdmin(ModelAdmin):
    """EquipmentGeneralType admin."""

    list_display = ('name',)

    show_full_result_count = False

    @silk_profile(name='Admin: Equipment General Types')
    def changelist_view(self, *args, **kwargs):
        """Change-list view."""
        return super().changelist_view(*args, **kwargs)

    @silk_profile(name='Admin: Equipment General Type')
    def changeform_view(self, *args, **kwargs):
        """Change-form view."""
        return super().changeform_view(*args, **kwargs)


@register(EquipmentDataField)
class EquipmentDataFieldAdmin(ModelAdmin):
    """EquipmentDataField admin."""

    list_display = (
        'equipment_general_type',
        'name',
        'equipment_data_field_type',
        'logical_data_type',
        'numeric_measurement_unit',
        'lower_numeric_null',
        'upper_numeric_null',
        'min_val',
        'max_val',
        'n_equipment_unique_types',
    )

    list_filter = (
        'equipment_general_type__name',
        'equipment_data_field_type__name',
        'logical_data_type__name',
        'numeric_measurement_unit__name',
        'lower_numeric_null',
        'upper_numeric_null',
        'name',
        'min_val',
        'max_val',
    )

    search_fields = (
        'equipment_general_type__name',
        'equipment_data_field_type__name',
        'name',
        'logical_data_type__name',
        'numeric_measurement_unit__name',
    )

    show_full_result_count = False

    def n_equipment_unique_types(self, obj):   # pylint: disable=no-self-use
        """Extra displayed field."""
        return obj.equipment_unique_types.count()

    def get_queryset(self, request):
        """Get queryset."""
        return super().get_queryset(request=request) \
            .select_related(
                'equipment_general_type',
                'equipment_data_field_type',
                'logical_data_type',
                'numeric_measurement_unit') \
            .prefetch_related(
                Prefetch(
                    lookup='equipment_unique_types',
                    queryset=EQUIPMENT_UNIQUE_TYPE_ID_ONLY_UNORDERED_QUERYSET))

    @silk_profile(name='Admin: Equipment Data Fields')
    def changelist_view(self, *args, **kwargs):
        """Change-list view."""
        return super().changelist_view(*args, **kwargs)

    @silk_profile(name='Admin: Equipment Data Field')
    def changeform_view(self, *args, **kwargs):
        """Change-form view."""
        return super().changeform_view(*args, **kwargs)


@register(EquipmentUniqueTypeGroup)
class EquipmentUniqueTypeGroupAdmin(ModelAdmin):
    """EquipmentUniqueTypeGroup admin."""

    list_display = (
        'equipment_general_type',
        'name',
        'equipment_unique_type_list',
        'n_equipment_data_fields',
        'n_equipment_instances',
    )

    list_filter = ('equipment_general_type__name',)

    search_fields = 'equipment_general_type__name', 'name'

    show_full_result_count = False

    readonly_fields = ('equipment_data_fields',)

    def equipment_unique_type_list(self, obj):   # pylint: disable=no-self-use
        """Extra displayed field."""
        n = obj.equipment_unique_types.count()
        return ((f'{n}: ' +
                 ', '.join(equipment_unique_type.name
                           for equipment_unique_type in
                           obj.equipment_unique_types.all()))
                if n
                else '')

    def n_equipment_data_fields(self, obj):   # pylint: disable=no-self-use
        """Extra displayed field."""
        return obj.equipment_data_fields.count()

    def n_equipment_instances(self, obj):   # pylint: disable=no-self-use
        """Extra displayed field."""
        return obj.equipment_instances.count()

    def get_queryset(self, request):
        """Get queryset."""
        qs = super().get_queryset(request=request) \
            .select_related(
                'equipment_general_type')

        return qs.prefetch_related(
            Prefetch(
                lookup='equipment_unique_types',
                queryset=EQUIPMENT_UNIQUE_TYPE_ID_ONLY_UNORDERED_QUERYSET),
            Prefetch(
                lookup='equipment_data_fields',
                queryset=EQUIPMENT_DATA_FIELD_STR_QUERYSET)) \
            if request.resolver_match.url_name.endswith('_change') \
            else qs.prefetch_related(
            Prefetch(
                lookup='equipment_unique_types',
                queryset=EQUIPMENT_UNIQUE_TYPE_NAME_ONLY_QUERYSET),
            Prefetch(
                lookup='equipment_data_fields',
                queryset=EQUIPMENT_DATA_FIELD_ID_ONLY_UNORDERED_QUERYSET),
            Prefetch(
                lookup='equipment_instances',
                queryset=EQUIPMENT_INSTANCE_ID_ONLY_UNORDERED_QUERYSET))

    @silk_profile(name='Admin: Equipment Unique Type Groups')
    def changelist_view(self, *args, **kwargs):
        """Change-list view."""
        return super().changelist_view(*args, **kwargs)

    @silk_profile(name='Admin: Equipment Unique Type Group')
    def changeform_view(self, *args, **kwargs):
        """Change-form view."""
        return super().changeform_view(*args, **kwargs)


@register(EquipmentUniqueType)
class EquipmentUniqueTypeAdmin(ModelAdmin):
    """EquipmentUniqueType admin."""

    list_display = (
        'equipment_general_type',
        'name',
        'n_equipment_data_fields',
        'equipment_unique_type_group_list',
        'n_equipment_instances',
    )

    list_filter = ('equipment_general_type__name',)

    show_full_result_count = False

    search_fields = 'equipment_general_type__name', 'name'

    def n_equipment_data_fields(self, obj):   # pylint: disable=no-self-use
        """Extra displayed field."""
        return obj.equipment_data_fields.count()

    def n_equipment_instances(self, obj):   # pylint: disable=no-self-use
        """Extra displayed field."""
        return obj.equipment_instances.count()

    def equipment_unique_type_group_list(self, obj):
        # pylint: disable=no-self-use
        """Extra displayed field."""
        n = obj.equipment_unique_type_groups.count()
        return ((f'{n}: ' +
                 ', '.join(equipment_unique_type_group.name
                           for equipment_unique_type_group in
                           obj.equipment_unique_type_groups.all()))
                if n
                else '')

    def get_queryset(self, request):
        """Get queryset."""
        qs = super().get_queryset(request=request) \
            .select_related(
                'equipment_general_type') \
            .prefetch_related(
                Prefetch(
                    lookup='equipment_data_fields',
                    queryset=EQUIPMENT_DATA_FIELD_ID_ONLY_UNORDERED_QUERYSET))

        return (
            qs.prefetch_related(
                Prefetch(
                    lookup='equipment_unique_type_groups',
                    queryset=EQUIPMENT_UNIQUE_TYPE_GROUP_ID_ONLY_UNORDERED_QUERYSET))   # noqa: E501
            ) if request.resolver_match.url_name.endswith('_change') \
            else qs.prefetch_related(
            Prefetch(
                lookup='equipment_instances',
                queryset=EQUIPMENT_INSTANCE_RELATED_TO_EQUIPMENT_UNIQUE_TYPE_ID_ONLY_UNORDERED_QUERYSET),   # noqa: E501
            Prefetch(
                lookup='equipment_unique_type_groups',
                queryset=EQUIPMENT_UNIQUE_TYPE_GROUP_NAME_ONLY_QUERYSET))

    @silk_profile(name='Admin: Equipment Unique Types')
    def changelist_view(self, *args, **kwargs):
        """Change-list view."""
        return super().changelist_view(*args, **kwargs)

    @silk_profile(name='Admin: Equipment Unique Type')
    def changeform_view(self, *args, **kwargs):
        """Change-form view."""
        return super().changeform_view(*args, **kwargs)


class EquipmentInstanceInLineFormSet(BaseInlineFormSet):
    """EquipmentInstanceInLineFormSet."""

    model = EquipmentInstance

    # def get_queryset(self):
    #     return super().get_queryset() \
    #         .select_related(
    #             'equipment_general_type',
    #             'equipment_unique_type',
    #             'equipment_unique_type__equipment_general_type')


class EquipmentInstanceTabularInline(TabularInline):
    """EquipmentInstanceTabularInline."""

    model = EquipmentInstance

    fields = 'equipment_general_type', 'equipment_unique_type', 'name'

    formset = EquipmentInstanceInLineFormSet

    extra = 0

    def get_queryset(self, request):
        """Get queryset."""
        return super().get_queryset(request=request) \
            .select_related(
                'equipment_general_type',
                'equipment_unique_type',
                'equipment_unique_type__equipment_general_type')


@register(EquipmentFacility)
class EquipmentFacilityAdmin(ModelAdmin):
    """EquipmentFacility admin."""

    list_display = (
        'name',
        'info',
        'n_equipment_instances',
    )

    search_fields = 'name', 'info'

    show_full_result_count = False

    # inlines = EquipmentInstanceTabularInline,

    def n_equipment_instances(self, obj):   # pylint: disable=no-self-use
        """Extra displayed field."""
        return obj.equipment_instances.count()

    def get_queryset(self, request):
        """Get queryset."""
        qs = super().get_queryset(request=request)

        return qs \
            if request.resolver_match.url_name.endswith('_change') \
            else qs.prefetch_related(
                Prefetch(
                    lookup='equipment_instances',
                    queryset=EQUIPMENT_INSTANCE_RELATED_TO_EQUIPMENT_FACILITY_ID_ONLY_UNORDERED_QUERYSET))   # noqa: E501

    @silk_profile(name='Admin: Equipment Facilities')
    def changelist_view(self, *args, **kwargs):
        """Change-list view."""
        return super().changelist_view(*args, **kwargs)

    @silk_profile(name='Admin: Equipment Facility')
    def changeform_view(self, *args, **kwargs):
        """Change-form view."""
        return super().changeform_view(*args, **kwargs)


@register(EquipmentInstance)
class EquipmentInstanceAdmin(ModelAdmin):
    """EquipmentInstance admin."""

    list_display = (
        'equipment_general_type',
        'equipment_unique_type',
        'equipment_facility',
        'name',
        'info',
    )

    list_filter = (
        'equipment_general_type__name',
        'equipment_unique_type__name',
        'equipment_facility__name',
    )

    search_fields = (
        'equipment_general_type__name',
        'equipment_unique_type__name',
        'equipment_facility__name',
        'name',
        'info',
    )

    show_full_result_count = False

    def get_queryset(self, request):
        """Get queryset."""
        qs = super().get_queryset(request=request)

        return (
            qs.select_related(
                'equipment_general_type',
                'equipment_unique_type')
            .defer(
                'equipment_unique_type__equipment_general_type')
            .prefetch_related(
                Prefetch(
                    lookup='equipment_unique_type_groups',
                    queryset=EQUIPMENT_UNIQUE_TYPE_GROUP_ID_ONLY_UNORDERED_QUERYSET))   # noqa: E501
            ) if request.resolver_match.url_name.endswith('_change') \
            else qs.select_related(
            'equipment_general_type',
            'equipment_unique_type',
            'equipment_unique_type__equipment_general_type',
            'equipment_facility') \
            .defer(
                'equipment_facility__info')

    @silk_profile(name='Admin: Equipment Instances')
    def changelist_view(self, *args, **kwargs):
        """Change-list view."""
        return super().changelist_view(*args, **kwargs)

    @silk_profile(name='Admin: Equipment Instance')
    def changeform_view(self, *args, **kwargs):
        """Change-form view."""
        return super().changeform_view(*args, **kwargs)


@register(EquipmentSystem)
class EquipmentSystemAdmin(ModelAdmin):
    """EquipmentSystem admin."""

    list_display = (
        'equipment_facility',
        'name',
        'date',
        'n_equipment_instances',
    )

    list_filter = 'equipment_facility__name', 'date'

    search_fields = 'equipment_facility__name', 'name'

    show_full_result_count = False

    def n_equipment_instances(self, obj):   # pylint: disable=no-self-use
        """Extra displayed field."""
        return obj.equipment_instances.count()

    def get_queryset(self, request):
        """Get queryset."""
        return super().get_queryset(request=request) \
            .select_related(
                'equipment_facility') \
            .defer(
                'equipment_facility__info') \
            .prefetch_related(
                Prefetch(
                    lookup='equipment_instances',
                    queryset=EQUIPMENT_INSTANCE_ID_ONLY_UNORDERED_QUERYSET))

    @silk_profile(name='Admin: Equipment Systems')
    def changelist_view(self, *args, **kwargs):
        """Change-list view."""
        return super().changelist_view(*args, **kwargs)

    @silk_profile(name='Admin: Equipment System')
    def changeform_view(self, *args, **kwargs):
        """Change-form view."""
        return super().changeform_view(*args, **kwargs)


@register(EquipmentUniqueTypeGroupDataFieldProfile)
class EquipmentUniqueTypeGroupDataFieldProfileAdmin(ModelAdmin):
    """EquipmentUniqueTypeGroupDataFieldProfile admin."""

    list_display = (
        'equipment_unique_type_group',
        'equipment_data_field',
        'to_date',
        'valid_proportion',
        'n_distinct_values',
        'distinct_values',
        'sample_min',
        'outlier_rst_min',
        'sample_quartile',
        'sample_median',
        'sample_3rd_quartile',
        'outlier_rst_max',
        'sample_max',
    )

    list_filter = (
        'equipment_unique_type_group__equipment_general_type__name',
        'equipment_unique_type_group__name',
        'to_date',
        'equipment_data_field__name',
    )

    search_fields = (
        'equipment_unique_type_group__equipment_general_type__name',
        'equipment_unique_type_group__name',
        'equipment_data_field__name',
    )

    show_full_result_count = False

    ordering = (
        'equipment_unique_type_group',
        '-to_date',
        '-n_distinct_values',
    )

    readonly_fields = (
        'equipment_unique_type_group',
        'equipment_data_field',
        'to_date',
        'valid_proportion',
        'n_distinct_values',
        'distinct_values',
        'sample_min',
        'outlier_rst_min',
        'sample_quartile',
        'sample_median',
        'sample_3rd_quartile',
        'outlier_rst_max',
        'sample_max',
    )

    def get_queryset(self, request):
        """Get queryset."""
        return super().get_queryset(request=request) \
            .select_related(
                'equipment_unique_type_group',
                'equipment_unique_type_group__equipment_general_type',
                'equipment_data_field',
                'equipment_data_field__equipment_general_type',
                'equipment_data_field__equipment_data_field_type',
                'equipment_data_field__logical_data_type',
                'equipment_data_field__numeric_measurement_unit')

    @silk_profile(
        name='Admin: Equipment Unique Type Group Data Field Profiles')
    def changelist_view(self, *args, **kwargs):
        """Change-list view."""
        return super().changelist_view(*args, **kwargs)

    @silk_profile(name='Admin: Equipment Unique Type Group Data Field Profile')
    def changeform_view(self, *args, **kwargs):
        """Change-form view."""
        return super().changeform_view(*args, **kwargs)
