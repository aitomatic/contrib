"""H1st IoT public API."""


import sys

from .data.models import (
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
from .maint_ops.models import (
    EquipmentInstanceDailyRiskScore,
    EquipmentProblemType,
    EquipmentInstanceDailyPredictedFault,
    EquipmentInstanceAlarmPeriod,
    EquipmentInstanceProblemDiagnosis,
    AlertDiagnosisStatus,
    EquipmentInstanceAlertPeriod,
)

if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = (
    'LogicalDataType',
    'NumericMeasurementUnit',
    'EquipmentDataFieldType',
    'EquipmentGeneralType',
    'EquipmentDataField',
    'EquipmentUniqueTypeGroup',
    'EquipmentUniqueType',
    'EquipmentFacility',
    'EquipmentInstance',
    'EquipmentSystem',
    'EquipmentUniqueTypeGroupDataFieldProfile',

    'EquipmentInstanceDailyRiskScore',
    'EquipmentProblemType',
    'EquipmentInstanceDailyPredictedFault',
    'EquipmentInstanceAlarmPeriod',
    'EquipmentInstanceProblemDiagnosis',
    'AlertDiagnosisStatus',
    'EquipmentInstanceAlertPeriod',
)
