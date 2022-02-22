"""Base Fault Prediction knowledge ("teacher") model class."""


from __future__ import annotations

from random import choice
from typing import Literal, Optional

from pandas import DataFrame

from h1st.model.oracle.teacher import Teacher

from h1st_contrib.pmfp.models.base import BaseFaultPredictor


class BaseFaultPredTeacher(BaseFaultPredictor, Teacher):
    # pylint: disable=abstract-method,too-many-ancestors
    """Base Fault Prediction knowledge ("teacher") model class."""

    def __init__(self,
                 general_type: Literal['refrig', 'disp_case'],
                 unique_type_group: str,
                 version: Optional[str] = None):
        """Init Fault Prediction knowledge ("teacher") model."""
        super().__init__(general_type=general_type,
                         unique_type_group=unique_type_group,
                         version=version)

    @classmethod
    def load(cls, version: str) -> BaseFaultPredTeacher:
        # pylint: disable=unused-argument
        """Load model artifacts by persisted model's version."""
        if cls is BaseFaultPredTeacher:
            # return an arbitrary model for testing
            return cls(general_type='refrig',
                       unique_type_group='co2_mid_1_compressor')

        raise NotImplementedError

    def predict(self, df_for_1_equipment_unit_for_1_day: DataFrame, /) -> bool:
        # pylint: disable=no-self-use,unused-argument
        """Fault Prediction logic.

        User shall override this method and return a boolean value indicating
        whether the equipment unit has the concerned fault on the date.
        """
        return choice((False, True))