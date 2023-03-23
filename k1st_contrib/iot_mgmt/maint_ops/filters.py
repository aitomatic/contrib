"""H1st IoT Maintenance Operations: filters."""


from rest_framework_filters import FilterSet, RelatedFilter

from h1st_contrib.iot_mgmt.data.models import (EquipmentUniqueTypeGroup,
                                               EquipmentInstance)
from h1st_contrib.iot_mgmt.data.filters import (EquipmentUniqueTypeGroupFilter,
                                                EquipmentInstanceFilter)
from h1st_contrib.iot_mgmt.maint_ops.models import (
    EquipmentInstanceDailyRiskScore,
    EquipmentProblemType,
    EquipmentInstanceAlarmPeriod,
    EquipmentInstanceProblemDiagnosis,
    AlertDiagnosisStatus,
    EquipmentInstanceAlertPeriod,
)


class EquipmentInstanceDailyRiskScoreFilter(FilterSet):
    """EquipmentInstanceDailyRiskScoreFilter."""

    equipment_unique_type_group = \
        RelatedFilter(
            queryset=EquipmentUniqueTypeGroup.objects.all(),
            filterset=EquipmentUniqueTypeGroupFilter)

    equipment_instance = \
        RelatedFilter(
            queryset=EquipmentInstance.objects.all(),
            filterset=EquipmentInstanceFilter)

    class Meta:
        """Metadata."""

        model = EquipmentInstanceDailyRiskScore

        fields = dict(
            risk_score_name=[
                'exact', 'iexact',
                'in',
                'contains', 'icontains',
                'startswith', 'istartswith', 'endswith', 'iendswith',
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
                'month__range',
            ],

            risk_score_value=[
                'gt', 'gte', 'lt', 'lte',
                'startswith', 'istartswith',
                'range',
            ])


class EquipmentProblemTypeFilter(FilterSet):
    """EquipmentProblemTypeFilter."""

    class Meta:
        """Metadata."""

        model = EquipmentProblemType

        fields = dict(
            name=[
                'exact', 'iexact',
                'in',
                'contains', 'icontains',
                'startswith', 'istartswith', 'endswith', 'iendswith',
            ])


class EquipmentInstanceAlarmPeriodFilter(FilterSet):
    """EquipmentInstanceAlarmPeriodFilter."""

    equipment_instance = \
        RelatedFilter(
            queryset=EquipmentInstance.objects.all(),
            filterset=EquipmentInstanceFilter)

    alarm_type = \
        RelatedFilter(
            queryset=EquipmentProblemType.objects.all(),
            filterset=EquipmentProblemTypeFilter)

    class Meta:
        """Metadata."""

        model = EquipmentInstanceAlarmPeriod

        fields = dict(
            from_utc_date_time=[
                'exact',   # 'iexact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',   # 'icontains'
                'startswith',   # 'istartswith'
                'endswith',   # 'iendswith',
                'range',
                'isnull',
                'year',   # 'year__iexact'
                'year__gt', 'year__gte', 'year__lt', 'year__lte',
                'year__in',
                'year__range',
                'month',   # 'month__iexact',
                'month__gt', 'month__gte', 'month__lt', 'month__lte',
                'month__in',
                'month__range',
            ],

            to_utc_date_time=[
                'exact',   # 'iexact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',   # 'icontains'
                'startswith',   # 'istartswith'
                'endswith',   # 'iendswith',
                'range',
                'isnull',
                'year',   # 'year__iexact'
                'year__gt', 'year__gte', 'year__lt', 'year__lte',
                'year__in',
                'year__range',
                'month',   # 'month__iexact',
                'month__gt', 'month__gte', 'month__lt', 'month__lte',
                'month__in',
                'month__range',
            ],

            duration_in_days=[
                'exact',   # 'iexact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',   # 'icontains',
                'startswith',   # 'istartswith',
                'endswith',   # 'iendswith',
                'range',
            ],

            has_associated_equipment_instance_alert_periods=['exact'],

            has_associated_equipment_instance_problem_diagnoses=['exact'])


class EquipmentInstanceProblemDiagnosisFilter(FilterSet):
    """EquipmentInstanceProblemDiagnosisFilter."""

    equipment_instance = \
        RelatedFilter(
            queryset=EquipmentInstance.objects.all(),
            filterset=EquipmentInstanceFilter)

    equipment_problem_types = \
        RelatedFilter(
            queryset=EquipmentProblemType.objects.all(),
            filterset=EquipmentProblemTypeFilter)

    class Meta:
        """Metadata."""

        model = EquipmentInstanceProblemDiagnosis

        fields = dict(
            from_date=[
                'exact',   # 'iexact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',   # 'icontains'
                'startswith',   # 'istartswith'
                'endswith',   # 'iendswith',
                'range',
                'isnull',
                'year',   # 'year__iexact'
                'year__gt', 'year__gte', 'year__lt', 'year__lte',
                'year__in',
                'year__range',
                'month',   # 'month__iexact',
                'month__gt', 'month__gte', 'month__lt', 'month__lte',
                'month__in',
                'month__range',
            ],

            to_date=[
                'exact',   # 'iexact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',   # 'icontains'
                'startswith',   # 'istartswith'
                'endswith',   # 'iendswith',
                'range',
                'isnull',
                'year',   # 'year__iexact'
                'year__gt', 'year__gte', 'year__lt', 'year__lte',
                'year__in',
                'year__range',
                'month',   # 'month__iexact',
                'month__gt', 'month__gte', 'month__lt', 'month__lte',
                'month__in',
                'month__range',
            ],

            duration=[
                'exact',   # 'iexact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',   # 'icontains',
                'startswith',   # 'istartswith',
                'endswith',   # 'iendswith',
                'range',
            ],

            has_equipment_problems=['exact'],

            dismissed=['exact'],

            has_associated_equipment_instance_alarm_periods=['exact'],

            has_associated_equipment_instance_alert_periods=['exact'])


class AlertDiagnosisStatusFilter(FilterSet):
    """AlertDiagnosisStatusFilter."""

    class Meta:
        """Metadata."""

        model = AlertDiagnosisStatus

        fields = dict(
            name=[
                'exact', 'iexact',
                'in',
                'contains', 'icontains',
                'startswith', 'istartswith', 'endswith', 'iendswith',
            ])


class EquipmentInstanceAlertPeriodFilter(FilterSet):
    """EquipmentInstanceAlertPeriodFilter."""

    equipment_unique_type_group = \
        RelatedFilter(
            queryset=EquipmentUniqueTypeGroup.objects.all(),
            filterset=EquipmentUniqueTypeGroupFilter)

    equipment_instance = \
        RelatedFilter(
            queryset=EquipmentInstance.objects.all(),
            filterset=EquipmentInstanceFilter)

    diagnosis_status = \
        RelatedFilter(
            queryset=AlertDiagnosisStatus.objects.all(),
            filterset=AlertDiagnosisStatusFilter)

    class Meta:
        """Metadata."""

        model = EquipmentInstanceAlertPeriod

        fields = dict(
            risk_score_name=[
                'exact', 'iexact',
                'in',
                'contains', 'icontains',
                'startswith', 'istartswith', 'endswith', 'iendswith',
            ],

            threshold=[
                'exact',   # 'iexact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',   # 'icontains',
                'startswith',   # 'istartswith',
                'endswith',   # 'iendswith',
                'range',
            ],

            from_date=[
                'exact',   # 'iexact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',   # 'icontains'
                'startswith',   # 'istartswith'
                'endswith',   # 'iendswith',
                'range',
                'isnull',
                'year',   # 'year__iexact'
                'year__gt', 'year__gte', 'year__lt', 'year__lte',
                'year__in',
                'year__range',
                'month',   # 'month__iexact',
                'month__gt', 'month__gte', 'month__lt', 'month__lte',
                'month__in',
                'month__range',
            ],

            to_date=[
                'exact',   # 'iexact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',   # 'icontains'
                'startswith',   # 'istartswith'
                'endswith',   # 'iendswith',
                'range',
                'isnull',
                'year',   # 'year__iexact'
                'year__gt', 'year__gte', 'year__lt', 'year__lte',
                'year__in',
                'year__range',
                'month',   # 'month__iexact',
                'month__gt', 'month__gte', 'month__lt', 'month__lte',
                'month__in',
                'month__range',
            ],

            duration=[
                'exact',   # 'iexact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',   # 'icontains',
                'startswith',   # 'istartswith',
                'endswith',   # 'iendswith',
                'range',
            ],

            cumulative_excess_risk_score=[
                'exact',   # 'iexact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',   # 'icontains',
                'startswith',   # 'istartswith',
                'endswith',   # 'iendswith',
                'range',
            ],

            approx_average_risk_score=[
                'exact',   # 'iexact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',   # 'icontains',
                'startswith',   # 'istartswith',
                'endswith',   # 'iendswith',
                'range',
            ],

            last_risk_score=[
                'exact',   # 'iexact',
                'gt', 'gte', 'lt', 'lte',
                'in',
                'contains',   # 'icontains',
                'startswith',   # 'istartswith',
                'endswith',   # 'iendswith',
                'range',
            ],

            ongoing=['exact'],

            has_associated_equipment_instance_alarm_periods=['exact'],

            has_associated_equipment_instance_problem_diagnoses=['exact'])
