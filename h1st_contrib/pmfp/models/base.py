"""Base Fault Prediction model class."""


from __future__ import annotations

from functools import cached_property
from logging import getLogger, Logger, DEBUG
import os
from random import random
import time
from typing import Literal, Optional, Union
from typing import Dict, List   # Py3.9+: use built-ins
from uuid import uuid4

from pandas import DataFrame, Series

from h1st.model.model import Model

from h1st_contrib.utils.data_proc import S3ParquetDataFeeder
from h1st_contrib.utils.log import STDOUT_HANDLER
from h1st_contrib.utils import s3

from h1st_contrib.pmfp.data_mgmt import (EquipmentParquetDataSet,
                                         EQUIPMENT_INSTANCE_ID_COL, DATE_COL)


__all__ = (
    'H1ST_MODELS_S3_DIR_PATH', 'H1ST_BATCH_OUTPUT_S3_DIR_PATH',

    'BaseFaultPredictor',
)


_S3_BUCKET: Optional[str] = os.environ.get('H1ST_PMFP_S3_BUCKET')


MODELS_S3_PREFIX: str = '.h1st/models'
H1ST_MODELS_S3_DIR_PATH: str = f's3://{_S3_BUCKET}/{MODELS_S3_PREFIX}'

BATCH_OUTPUT_S3_PREFIX: str = '.h1st/batch-output'
H1ST_BATCH_OUTPUT_S3_DIR_PATH: str = f's3://{_S3_BUCKET}/{BATCH_OUTPUT_S3_PREFIX}'   # noqa: E501


class BaseFaultPredictor(Model):
    # pylint: disable=too-many-ancestors
    """Base Fault Prediction model class."""

    def __init__(self,
                 general_type: Literal['refrig', 'disp_case'],
                 unique_type_group: str,
                 version: Optional[str] = None):
        # pylint: disable=super-init-not-called
        """Init Fault Prediction model."""
        self.general_type: str = general_type
        self.unique_type_group: str = unique_type_group
        self.version: str = version if version else str(uuid4())

    def __repr__(self) -> str:
        """Return string repr."""
        return f'{self.unique_type_group} {type(self).__name__} "{self.version}"'   # noqa: E501

    @cached_property
    def name(self) -> str:
        """Return string name."""
        return f'{type(self).__name__}--{self.version}'

    @property
    def logger(self) -> Logger:
        """Logger."""
        logger: Logger = getLogger(name=str(self))
        logger.setLevel(level=DEBUG)
        logger.addHandler(hdlr=STDOUT_HANDLER)
        return logger

    def save(self):
        """Persist model instance."""
        raise NotImplementedError

    @classmethod
    def load(cls, version: str) -> BaseFaultPredictor:
        # pylint: disable=unused-argument
        """Load model instance by version."""
        if cls is BaseFaultPredictor:
            # return an arbitrary model for testing
            return cls(general_type='refrig',
                       unique_type_group='co2_mid_1_compressor')

        raise NotImplementedError

    @classmethod
    def list_versions(cls) -> List[str]:
        """List model versions."""
        assert _S3_BUCKET, \
            EnvironmentError('*** H1ST_PMFP_S3_BUCKET env var not set ***')

        prefix_len: int = len(prefix := f'{MODELS_S3_PREFIX}/{cls.__name__}/')

        results: dict = s3.client().list_objects_v2(Bucket=_S3_BUCKET,
                                                    Delimiter='/',
                                                    EncodingType='url',
                                                    MaxKeys=10 ** 3,
                                                    Prefix=prefix)

        return [i['Prefix'][prefix_len:-1]
                for i in results.get('CommonPrefixes', [])]

    def predict(self, df_for_1_equipment_unit_for_1_day: DataFrame, /) \
            -> Union[bool, float]:
        # pylint: disable=no-self-use,unused-argument
        """Fault Prediction logic.

        User shall override this method and return a boolean or float value for
        whether the equipment unit has the concerned fault on the date.
        """
        return random()

    def batch_predict(self,
                      s3_parquet_df: S3ParquetDataFeeder, /,
                      **predict_kwargs) -> Series:
        """Batch predict."""
        return s3_parquet_df.map(
            lambda df: (df.groupby(by=[EQUIPMENT_INSTANCE_ID_COL, DATE_COL],
                                   axis='index',
                                   level=None,
                                   as_index=True,   # group labels as index
                                   sort=False,   # better performance
                                   # when `apply`ing: add group keys to index?
                                   group_keys=False,
                                   # squeeze=False,   # deprecated
                                   observed=False,
                                   dropna=True)
                        .apply(func=self.predict, **predict_kwargs))).collect()

    def batch_process(self,
                      date: str, to_date: Optional[str] = None,
                      *, equipment_instance_id: Optional[str] = None,
                      return_json: bool = False, **predict_kwargs) \
            -> Union[Series,
                     Dict[str, Dict[str, Union[bool, float]]]]:
        # pylint: disable=too-many-locals
        """(Bulk-)Process data to predict fault per equipment unit per date."""
        try:
            s3_parquet_df: S3ParquetDataFeeder = (
                EquipmentParquetDataSet(general_type=self.general_type,
                                        unique_type_group=self.unique_type_group)   # noqa: E501
                .load_by_date(date=date, to_date=to_date,
                              equipment_instance_id=equipment_instance_id))

        except Exception as err:   # pylint: disable=broad-except
            print(f'*** {err} ***')

            return ({}
                    if return_json
                    else (DataFrame(columns=[EQUIPMENT_INSTANCE_ID_COL, DATE_COL,   # noqa: E501
                                             'FAULT'])
                          .set_index(keys=[EQUIPMENT_INSTANCE_ID_COL, DATE_COL],   # noqa: E501
                                     drop=True,
                                     append=False,
                                     verify_integrity=True,
                                     inplace=False)))

        s3_parquet_df.cacheLocally()

        self.logger.info(
            msg=(msg := f'Batch-Processing {s3_parquet_df.__shortRepr__}...'))
        tic: float = time.time()

        fault_preds: Series = (self.batch_predict(s3_parquet_df, **predict_kwargs)  # noqa: E501
                               # sort index to make output order consistent
                               .sort_index(axis='index',
                                           level=None,
                                           ascending=True,
                                           inplace=False,
                                           kind='quicksort',
                                           na_position='last',
                                           sort_remaining=True,
                                           ignore_index=False,
                                           key=None))

        toc: float = time.time()
        self.logger.info(msg=f'{msg} done!   <{toc-tic:.1f}s>')

        if return_json:
            d: Dict[str, Dict[str, Union[bool, float]]] = {}

            for (_equipment_instance_id, _date), pred in fault_preds.items():
                if isinstance(pred, tuple):
                    assert len(pred) == 3
                    pred: List[Union[bool, float]] = [bool(i) for i in pred]

                if _equipment_instance_id in d:
                    d[_equipment_instance_id][str(_date)] = pred
                else:
                    d[_equipment_instance_id] = {str(_date): pred}

            return d

        return fault_preds