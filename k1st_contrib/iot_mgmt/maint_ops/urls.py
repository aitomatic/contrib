"""H1st IoT Maintenance Operations: URL configs."""


from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from h1st_contrib.iot_mgmt.maint_ops.views import (
    EquipmentInstanceDailyRiskScoreViewSet,
    EquipmentProblemTypeViewSet,
    EquipmentInstanceAlarmPeriodViewSet,
    EquipmentInstanceProblemDiagnosisViewSet,
    AlertDiagnosisStatusViewSet,
    EquipmentInstanceAlertPeriodViewSet,
)


ROUTER = DefaultRouter()

ROUTER.register(
    'equipment-instance-daily-risk-scores',
    EquipmentInstanceDailyRiskScoreViewSet)

ROUTER.register(
    'equipment-problem-types',
    EquipmentProblemTypeViewSet)

ROUTER.register(
    'equipment-instance-alarm-periods',
    EquipmentInstanceAlarmPeriodViewSet)

ROUTER.register(
    'equipment-instance-problem-diagnoses',
    EquipmentInstanceProblemDiagnosisViewSet)

ROUTER.register(
    'alert-diagnosis-statuses',
    AlertDiagnosisStatusViewSet)

ROUTER.register(
    'equipment-instance-alert-periods',
    EquipmentInstanceAlertPeriodViewSet)


URL_PATTERNS = [
    # API URLs
    url('iot/api/maint-ops/', include(ROUTER.urls)),
]
