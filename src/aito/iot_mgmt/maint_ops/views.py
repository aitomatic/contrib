"""H1st IoT Data Management: API views."""


from rest_framework.authentication import (BasicAuthentication,
                                           RemoteUserAuthentication,
                                           SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.renderers import CoreJSONRenderer, JSONRenderer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from silk.profiling.profiler import silk_profile

from k1st_contrib.iot_mgmt.maint_ops.filters import (
    EquipmentInstanceDailyRiskScoreFilter,
    EquipmentProblemTypeFilter,
    EquipmentInstanceAlarmPeriodFilter,
    EquipmentInstanceProblemDiagnosisFilter,
    AlertDiagnosisStatusFilter,
    EquipmentInstanceAlertPeriodFilter,
)
from k1st_contrib.iot_mgmt.maint_ops.querysets import (
    EQUIPMENT_INSTANCE_DAILY_RISK_SCORE,
    EQUIPMENT_PROBLEM_TYPE_QUERYSET,
    EQUIPMENT_INSTANCE_ALARM_PERIOD_REST_API_QUERYSET,
    ALERT_DIAGNOSIS_STATUS_REST_API_QUERYSET,
    EQUIPMENT_INSTANCE_ALERT_PERIOD_REST_API_QUERYSET,
    EQUIPMENT_INSTANCE_PROBLEM_DIAGNOSIS_REST_API_QUERYSET,
)
from k1st_contrib.iot_mgmt.maint_ops.serializers import (
    EquipmentInstanceDailyRiskScoreSerializer,
    EquipmentProblemTypeSerializer,
    EquipmentInstanceAlarmPeriodSerializer,
    EquipmentInstanceProblemDiagnosisSerializer,
    AlertDiagnosisStatusSerializer,
    EquipmentInstanceAlertPeriodSerializer,
)


class EquipmentInstanceDailyRiskScoreViewSet(ReadOnlyModelViewSet):
    """EquipmentInstanceDailyRiskScoreViewSet.

    list:
    `GET` a filterable, paginated list of Equipment Instance Daily Risk Scores

    retrieve:
    `GET` the Equipment Instance Daily Risk Score specified by `id`
    """

    queryset = EQUIPMENT_INSTANCE_DAILY_RISK_SCORE

    serializer_class = EquipmentInstanceDailyRiskScoreSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = (IsAuthenticated,)

    filter_class = EquipmentInstanceDailyRiskScoreFilter

    ordering_fields = \
        'equipment_unique_type_group', \
        'equipment_instance', \
        'risk_score_name', \
        'date'

    pagination_class = LimitOffsetPagination

    renderer_classes = CoreJSONRenderer, JSONRenderer

    @silk_profile(name='API: Equipment Instance Daily Risk Scores')
    def list(self, request, *args, **kwargs):
        """List items."""
        return super().list(request, *args, **kwargs)

    @silk_profile(name='API: Equipment Instance Daily Risk Score')
    def retrieve(self, request, *args, **kwargs):
        """Retrieve item."""
        return super().retrieve(request, *args, **kwargs)


class EquipmentProblemTypeViewSet(ModelViewSet):
    """EquipmentProblemTypeViewSet.

    list:
    `GET` a filterable, unpaginated list of Equipment Problem Types

    retrieve:
    `GET` the Equipment Problem Type specified by `name`

    create:
    `POST` a new Equipment Problem Type by `name`

    update:
    `PUT` updated data for the Equipment Problem Type specified by `name`

    partial_update:
    `PATCH` the Equipment Problem Type specified by `name`

    destroy:
    `DELETE` the Equipment Problem Type specified by `name`
    """

    queryset = EQUIPMENT_PROBLEM_TYPE_QUERYSET

    serializer_class = EquipmentProblemTypeSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = (IsAuthenticated,)

    filter_class = EquipmentProblemTypeFilter

    ordering_fields = ('name',)

    ordering = ('name',)

    pagination_class = None

    lookup_field = 'name'

    lookup_url_kwarg = 'equipment_problem_type_name'

    renderer_classes = CoreJSONRenderer, JSONRenderer

    @silk_profile(name='API: Equipment Problem Types')
    def list(self, request, *args, **kwargs):
        """List items."""
        return super().list(request, *args, **kwargs)

    @silk_profile(name='API: Equipment Problem Type')
    def retrieve(self, request, *args, **kwargs):
        """Retrieve item."""
        return super().retrieve(request, *args, **kwargs)


class EquipmentInstanceAlarmPeriodViewSet(ModelViewSet):
    """EquipmentInstanceAlarmPeriodViewSet."""

    queryset = EQUIPMENT_INSTANCE_ALARM_PERIOD_REST_API_QUERYSET

    serializer_class = EquipmentInstanceAlarmPeriodSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = (IsAuthenticated,)

    filter_class = EquipmentInstanceAlarmPeriodFilter

    ordering_fields = \
        'equipment_instance', \
        'from_utc_date_time'

    ordering = \
        '-from_utc_date_time'

    pagination_class = LimitOffsetPagination

    renderer_classes = CoreJSONRenderer, JSONRenderer

    @silk_profile(name='API: Equipment Instance Alarm Periods')
    def list(self, request, *args, **kwargs):
        """List items."""
        return super().list(request, *args, **kwargs)

    @silk_profile(name='API: Equipment Instance Alarm Period')
    def retrieve(self, request, *args, **kwargs):
        """Retrieve item."""
        return super().retrieve(request, *args, **kwargs)


class EquipmentInstanceProblemDiagnosisViewSet(ModelViewSet):
    """EquipmentInstanceProblemDiagnosisViewSet."""

    queryset = EQUIPMENT_INSTANCE_PROBLEM_DIAGNOSIS_REST_API_QUERYSET

    serializer_class = EquipmentInstanceProblemDiagnosisSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = (IsAuthenticated,)

    filter_class = EquipmentInstanceProblemDiagnosisFilter

    ordering_fields = \
        'ongoing', \
        'from_date', \
        'to_date', \
        'equipment_instance', \
        'dismissed'

    ordering = \
        '-ongoing', \
        '-from_date', \
        '-to_date', \
        'dismissed'

    pagination_class = LimitOffsetPagination

    renderer_classes = CoreJSONRenderer, JSONRenderer

    @silk_profile(name='API: Equipment Instance Problem Diagnoses')
    def list(self, request, *args, **kwargs):
        """List items."""
        return super().list(request, *args, **kwargs)

    @silk_profile(name='API: Equipment Instance Problem Diagnosis')
    def retrieve(self, request, *args, **kwargs):
        """Retrieve item."""
        return super().retrieve(request, *args, **kwargs)


class AlertDiagnosisStatusViewSet(ReadOnlyModelViewSet):
    """AlertDiagnosisStatusViewSet.

    list:
    `GET` a filterable, unpaginated list of Alert Diagnosis Statuses

    retrieve:
    `GET` the Alert Diagnosis Status specified by `name`
    """

    queryset = ALERT_DIAGNOSIS_STATUS_REST_API_QUERYSET

    serializer_class = AlertDiagnosisStatusSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_class = AlertDiagnosisStatusFilter

    ordering_fields = ('index',)

    ordering = ('index',)

    pagination_class = None

    lookup_field = 'name'

    lookup_url_kwarg = 'alert_diagnosis_status_name'

    renderer_classes = CoreJSONRenderer, JSONRenderer

    @silk_profile(name='API: Alert Diagnosis Statuses')
    def list(self, request, *args, **kwargs):
        """List items."""
        return super().list(request, *args, **kwargs)

    @silk_profile(name='API: Alert Diagnosis Status')
    def retrieve(self, request, *args, **kwargs):
        """Retrieve item."""
        return super().retrieve(request, *args, **kwargs)


class EquipmentInstanceAlertPeriodViewSet(ModelViewSet):
    """EquipmentInstanceAlertPeriodViewSet.

    list:
    `GET` a filterable, paginated list of Alerts

    retrieve:
    `GET` the Alert specified by `id`

    partial_update:
    `PATCH` the `diagnosis_status` of the Alert specified by `id`
    """

    queryset = EQUIPMENT_INSTANCE_ALERT_PERIOD_REST_API_QUERYSET

    serializer_class = EquipmentInstanceAlertPeriodSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = (IsAuthenticated,)

    filter_class = EquipmentInstanceAlertPeriodFilter

    ordering_fields = \
        'diagnosis_status', \
        'ongoing', \
        'risk_score_name', \
        'threshold', \
        'cumulative_excess_risk_score'

    ordering = \
        'diagnosis_status', \
        '-ongoing', \
        'risk_score_name', \
        '-threshold', \
        '-cumulative_excess_risk_score'

    pagination_class = LimitOffsetPagination

    renderer_classes = CoreJSONRenderer, JSONRenderer

    @silk_profile(name='API: Equipment Instance Alert Periods')
    def list(self, request, *args, **kwargs):
        """List items."""
        return super().list(request, *args, **kwargs)

    @silk_profile(name='API: Equipment Instance Alert Period')
    def retrieve(self, request, *args, **kwargs):
        """Retrieve item."""
        return super().retrieve(request, *args, **kwargs)
