"""H1st IoT Maintenance Operations: serializers."""


from rest_framework.serializers import (ModelSerializer,
                                        RelatedField,
                                        SlugRelatedField)

from drf_writable_nested.serializers import WritableNestedModelSerializer

from k1st_contrib.iot_mgmt.data.models import EquipmentInstance

from k1st_contrib.iot_mgmt.maint_ops.models import (
    EquipmentInstanceDailyRiskScore,
    EquipmentProblemType,
    EquipmentInstanceAlarmPeriod,
    EquipmentInstanceProblemDiagnosis,
    AlertDiagnosisStatus,
    EquipmentInstanceAlertPeriod,
)


class EquipmentInstanceDailyRiskScoreSerializer(ModelSerializer):
    """EquipmentInstanceDailyRiskScoreSerializer."""

    equipment_unique_type_group = \
        SlugRelatedField(
            read_only=True,
            slug_field='name',
            many=False)

    equipment_instance = \
        SlugRelatedField(
            read_only=True,
            slug_field='name',
            many=False)

    class Meta:
        """Metadata."""

        model = EquipmentInstanceDailyRiskScore

        fields = \
            'id', \
            'equipment_unique_type_group', \
            'equipment_instance', \
            'risk_score_name', \
            'date', \
            'risk_score_value'


class EquipmentProblemTypeSerializer(ModelSerializer):
    """EquipmentProblemTypeSerializer."""

    class Meta:
        """Metadata."""

        model = EquipmentProblemType

        fields = ('name',)


class EquipmentInstanceAlarmPeriodRelatedField(RelatedField):
    # pylint: disable=abstract-method
    """EquipmentInstanceAlarmPeriodRelatedField."""

    def to_representation(self, value):
        """Get representation."""
        return dict(
            equipment_instance=value.equipment_instance.name,
            alarm_type=value.alarm_type.name,
            from_utc_date_time=str(value.from_utc_date_time),
            to_utc_date_time=str(value.to_utc_date_time),
            duration_in_days=value.duration_in_days,
            has_associated_equipment_instance_alert_periods=   # noqa: E251
            value.has_associated_equipment_instance_alert_periods,
            has_associated_equipment_instance_problem_diagnoses=   # noqa: E251
            value.has_associated_equipment_instance_problem_diagnoses)


class EquipmentInstanceProblemDiagnosisRelatedField(RelatedField):
    # pylint: disable=abstract-method
    """EquipmentInstanceProblemDiagnosisRelatedField."""

    def to_representation(self, value):
        """Get representation."""
        return dict(
            equipment_instance=value.equipment_instance.name,
            from_date=str(value.from_date),
            to_date=str(value.to_date),
            duration=value.duration,
            has_equipment_problems=value.has_equipment_problems,
            equipment_problem_types=[i.name
                                     for i in
                                     value.equipment_problem_types.all()],
            dismissed=value.dismissed,
            comments=value.comments,
            has_associated_equipment_instance_alarm_periods=   # noqa: E251
            value.has_associated_equipment_instance_alarm_periods,
            has_associated_equipment_instance_alert_periods=   # noqa: E251
            value.has_associated_equipment_instance_alert_periods)


class EquipmentInstanceAlertPeriodRelatedField(RelatedField):
    # pylint: disable=abstract-method
    """EquipmentInstanceAlertPeriodRelatedField."""

    def to_representation(self, value):
        """Get representation."""
        return dict(
            equipment_unique_type_group=value.equipment_unique_type_group.name,
            equipment_instance=value.equipment_instance.name,
            risk_score_name=value.risk_score_name,
            threshold=value.threshold,
            from_date=str(value.from_date),
            to_date=str(value.to_date),
            duration=value.duration,
            cumulative_excess_risk_score=value.cumulative_excess_risk_score,
            approx_average_risk_score=value.approx_average_risk_score,
            last_risk_score=value.last_risk_score,
            ongoing=value.ongoing,
            info=value.info,
            diagnosis_status=value.diagnosis_status.name,
            has_associated_equipment_instance_alarm_periods=   # noqa: E251
            value.has_associated_equipment_instance_alarm_periods,
            has_associated_equipment_instance_problem_diagnoses=   # noqa: E251
            value.has_associated_equipment_instance_problem_diagnoses)


class EquipmentInstanceAlarmPeriodSerializer(WritableNestedModelSerializer):
    """EquipmentInstanceAlarmPeriodSerializer."""

    equipment_instance = \
        SlugRelatedField(
            queryset=EquipmentInstance.objects.all(), read_only=False,
            slug_field='name',
            many=False,
            required=True)

    alarm_type = \
        SlugRelatedField(
            queryset=EquipmentProblemType.objects.all(), read_only=False,
            slug_field='name',
            many=False,
            required=True)

    equipment_instance_alert_periods = \
        EquipmentInstanceAlertPeriodRelatedField(
            read_only=True,
            many=True)

    equipment_instance_problem_diagnoses = \
        EquipmentInstanceProblemDiagnosisRelatedField(
            read_only=True,
            many=True)

    class Meta:
        """Metadata."""

        model = EquipmentInstanceAlarmPeriod

        fields = \
            'id', \
            'equipment_instance', \
            'alarm_type', \
            'from_utc_date_time', \
            'to_utc_date_time', \
            'duration_in_days', \
            'has_associated_equipment_instance_alert_periods', \
            'equipment_instance_alert_periods', \
            'has_associated_equipment_instance_problem_diagnoses', \
            'equipment_instance_problem_diagnoses'


class EquipmentInstanceProblemDiagnosisSerializer(
        WritableNestedModelSerializer):
    """EquipmentInstanceProblemDiagnosisSerializer."""

    equipment_instance = \
        SlugRelatedField(
            queryset=EquipmentInstance.objects.all(), read_only=False,
            slug_field='name',
            many=False,
            required=True)

    equipment_problem_types = \
        SlugRelatedField(
            queryset=EquipmentProblemType.objects.all(), read_only=False,
            slug_field='name',
            many=True,
            required=True)

    equipment_instance_alarm_periods = \
        EquipmentInstanceAlarmPeriodRelatedField(
            read_only=True,
            many=True)

    equipment_instance_alert_periods = \
        EquipmentInstanceAlertPeriodRelatedField(
            read_only=True,
            many=True)

    class Meta:
        """Metadata."""

        model = EquipmentInstanceProblemDiagnosis

        fields = \
            'id', \
            'equipment_instance', \
            'from_date', \
            'to_date', \
            'duration', \
            'ongoing', \
            'equipment_problem_types', \
            'has_equipment_problems', \
            'dismissed', \
            'comments', \
            'has_associated_equipment_instance_alarm_periods', \
            'equipment_instance_alarm_periods', \
            'has_associated_equipment_instance_alert_periods', \
            'equipment_instance_alert_periods'


class AlertDiagnosisStatusSerializer(ModelSerializer):
    """AlertDiagnosisStatusSerializer."""

    class Meta:
        """Metadata."""

        model = AlertDiagnosisStatus

        fields = ('name',)


class EquipmentInstanceAlertPeriodSerializer(ModelSerializer):
    """EquipmentInstanceAlertPeriodSerializer."""

    equipment_unique_type_group = \
        SlugRelatedField(
            read_only=True,
            slug_field='name',
            many=False)

    equipment_instance = \
        SlugRelatedField(
            read_only=True,
            slug_field='name',
            many=False)

    diagnosis_status = \
        SlugRelatedField(
            queryset=AlertDiagnosisStatus.objects.all(), read_only=False,
            slug_field='name',
            many=False,
            required=False)

    equipment_instance_alarm_periods = \
        EquipmentInstanceAlarmPeriodRelatedField(
            read_only=True,
            many=True)

    equipment_instance_problem_diagnoses = \
        EquipmentInstanceProblemDiagnosisRelatedField(
            read_only=True,
            many=True)

    class Meta:
        """Metadata."""

        model = EquipmentInstanceAlertPeriod

        fields = \
            'id', \
            'equipment_unique_type_group', \
            'equipment_instance', \
            'risk_score_name', \
            'threshold', \
            'from_date', \
            'to_date', \
            'duration', \
            'cumulative_excess_risk_score', \
            'approx_average_risk_score', \
            'last_risk_score', \
            'ongoing', \
            'info', \
            'diagnosis_status', \
            'has_associated_equipment_instance_alarm_periods', \
            'equipment_instance_alarm_periods', \
            'has_associated_equipment_instance_problem_diagnoses', \
            'equipment_instance_problem_diagnoses'
