"""H1st IoT Maintenance Operations: querysets."""


from django.db.models import Prefetch

from h1st_contrib.iot_mgmt.maint_ops.models import (
    EquipmentInstanceDailyRiskScore,
    EquipmentProblemType,
    EquipmentInstanceAlarmPeriod,
    AlertDiagnosisStatus,
    EquipmentInstanceAlertPeriod,
    EquipmentInstanceProblemDiagnosis,
)


EQUIPMENT_INSTANCE_DAILY_RISK_SCORE = \
    EquipmentInstanceDailyRiskScore.objects \
    .select_related(
        'equipment_unique_type_group',
        'equipment_instance') \
    .defer(
        'equipment_unique_type_group__equipment_general_type',
        'equipment_instance__equipment_general_type',
        'equipment_instance__equipment_unique_type',
        'equipment_instance__equipment_facility',
        'equipment_instance__info')


EQUIPMENT_PROBLEM_TYPE_QUERYSET = \
    EquipmentProblemType.objects.all()


EQUIPMENT_INSTANCE_ALARM_PERIOD_STR_QUERYSET = \
    EquipmentInstanceAlarmPeriod.objects \
    .defer(
        'date_range',
        'has_associated_equipment_instance_alert_periods',
        'has_associated_equipment_instance_problem_diagnoses') \
    .select_related(
        'equipment_instance',
        'equipment_instance__equipment_general_type',
        'equipment_instance__equipment_unique_type',
        'alarm_type') \
    .defer(
        'equipment_instance__equipment_facility',
        'equipment_instance__info') \
    .order_by(
        'from_utc_date_time')


EQUIPMENT_INSTANCE_ALARM_PERIOD_FULL_QUERYSET = \
    EquipmentInstanceAlarmPeriod.objects \
    .defer(
        'date_range') \
    .select_related(
        'equipment_instance',
        'alarm_type') \
    .defer(
        'equipment_instance__equipment_general_type',
        'equipment_instance__equipment_unique_type',
        'equipment_instance__equipment_facility',
        'equipment_instance__info') \
    .order_by(
        'from_utc_date_time')


ALERT_DIAGNOSIS_STATUS_REST_API_QUERYSET = \
    AlertDiagnosisStatus.objects.all()


EQUIPMENT_INSTANCE_ALERT_PERIOD_STR_QUERYSET = \
    EquipmentInstanceAlertPeriod.objects \
    .defer(
        'date_range',
        'info',
        'has_associated_equipment_instance_alarm_periods',
        'has_associated_equipment_instance_problem_diagnoses') \
    .select_related(
        'equipment_unique_type_group',
        'equipment_unique_type_group__equipment_general_type',
        'equipment_instance',
        'diagnosis_status') \
    .defer(
        'equipment_instance__equipment_general_type',
        'equipment_instance__equipment_unique_type',
        'equipment_instance__equipment_facility',
        'equipment_instance__info',
        'diagnosis_status__index')


EQUIPMENT_INSTANCE_ALERT_PERIOD_FULL_QUERYSET = \
    EquipmentInstanceAlertPeriod.objects \
    .defer(
        'date_range') \
    .select_related(
        'equipment_unique_type_group',
        'equipment_instance',
        'diagnosis_status') \
    .defer(
        'equipment_unique_type_group__equipment_general_type',
        'equipment_instance__equipment_general_type',
        'equipment_instance__equipment_unique_type',
        'equipment_instance__equipment_facility',
        'equipment_instance__info',
        'diagnosis_status__index')


EQUIPMENT_INSTANCE_PROBLEM_DIAGNOSIS_ID_ONLY_UNORDERED_QUERYSET = \
    EquipmentInstanceProblemDiagnosis.objects \
    .only('id') \
    .order_by()


EQUIPMENT_INSTANCE_PROBLEM_DIAGNOSIS_STR_QUERYSET = \
    EquipmentInstanceProblemDiagnosis.objects \
    .defer(
        'date_range',
        'duration',
        'has_equipment_problems',
        'comments',
        'has_associated_equipment_instance_alarm_periods',
        'has_associated_equipment_instance_alert_periods') \
    .select_related(
        'equipment_instance',
        'equipment_instance__equipment_general_type',
        'equipment_instance__equipment_unique_type') \
    .defer(
        'equipment_instance__equipment_facility',
        'equipment_instance__info') \
    .prefetch_related(
        'equipment_problem_types')


EQUIPMENT_INSTANCE_PROBLEM_DIAGNOSIS_FULL_QUERYSET = \
    EquipmentInstanceProblemDiagnosis.objects \
    .defer(
        'date_range') \
    .select_related(
        'equipment_instance') \
    .defer(
        'equipment_instance__equipment_general_type',
        'equipment_instance__equipment_unique_type',
        'equipment_instance__equipment_facility',
        'equipment_instance__info') \
    .prefetch_related(
        'equipment_problem_types')


EQUIPMENT_INSTANCE_ALARM_PERIOD_REST_API_QUERYSET = \
    EQUIPMENT_INSTANCE_ALARM_PERIOD_FULL_QUERYSET \
    .prefetch_related(
        Prefetch(
            lookup='equipment_instance_alert_periods',
            queryset=EQUIPMENT_INSTANCE_ALERT_PERIOD_FULL_QUERYSET),
        Prefetch(
            lookup='equipment_instance_problem_diagnoses',
            queryset=EQUIPMENT_INSTANCE_PROBLEM_DIAGNOSIS_FULL_QUERYSET))


EQUIPMENT_INSTANCE_ALERT_PERIOD_REST_API_QUERYSET = \
    EQUIPMENT_INSTANCE_ALERT_PERIOD_FULL_QUERYSET \
    .prefetch_related(
        Prefetch(
            lookup='equipment_instance_alarm_periods',
            queryset=EQUIPMENT_INSTANCE_ALARM_PERIOD_FULL_QUERYSET),
        Prefetch(
            lookup='equipment_instance_problem_diagnoses',
            queryset=EQUIPMENT_INSTANCE_PROBLEM_DIAGNOSIS_FULL_QUERYSET))


EQUIPMENT_INSTANCE_PROBLEM_DIAGNOSIS_REST_API_QUERYSET = \
    EQUIPMENT_INSTANCE_PROBLEM_DIAGNOSIS_FULL_QUERYSET \
    .prefetch_related(
        Prefetch(
            lookup='equipment_instance_alarm_periods',
            queryset=EQUIPMENT_INSTANCE_ALARM_PERIOD_FULL_QUERYSET),
        Prefetch(
            lookup='equipment_instance_alert_periods',
            queryset=EQUIPMENT_INSTANCE_ALERT_PERIOD_FULL_QUERYSET))
