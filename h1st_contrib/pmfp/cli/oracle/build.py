"""Oraclize a Fault-Prediction Knowledge ("Teacher") model.

Example:
AWS_ACCESS_KEY_ID=<...aws-access-key-id...> \
AWS_SECRET_ACCESS_KEY=<...aws-secret-access-key...> \
    h1st pmfp oraclize-fault-pred-teacher \
    My1stFaultPredTeacher <...teacher-model-version...> \
    \
    --input-cat-cols compressor1 compressor2 compressor3 \
    --input-num-cols high_pressure low_pressure \
    \
    --train-date-range 2016-09-01 2020-12-31 \
    --tune-date-range 2021-01-01 2021-12-31
"""


from typing import Optional
from typing import Collection, Tuple   # Py3.9+: use built-ins/collections.abc

import click

from h1st_contrib.pmfp.models import BaseFaultPredTeacher, FaultPredOracleModeler   # noqa: E501

import h1st_contrib.utils.debug


@click.command(name='oraclize-fault-pred-teacher',
               cls=click.Command)
def oraclize_fault_pred_teacher(
        teacher_class_name: str, teacher_version: str,
        input_cat_cols: Optional[Collection[str]],
        input_num_cols: Optional[Collection[str]],
        input_subsampling_factor: int,
        train_date_range: Tuple[str, str], tune_date_range: Tuple[str, str],
        debug: bool = False):
    """Oraclize a Fault-Prediction Knowledge ("Teacher") model."""
    assert input_cat_cols or input_num_cols

    if debug:
        h1st_contrib.utils.debug.ON = True

    # load Teacher model
    import ai.models   # pylint: disable=import-error,import-outside-toplevel

    teacher: BaseFaultPredTeacher = (getattr(ai.models, teacher_class_name)
                                     .load(version=teacher_version))

    # oraclize Teacher model
    FaultPredOracleModeler(
        teacher=teacher,

        student_input_cat_cols=input_cat_cols,
        student_input_num_cols=input_num_cols,
        student_input_subsampling_factor=input_subsampling_factor,

        student_train_date_range=train_date_range,
        student_tuning_date_range=tune_date_range,

    ).build_model()
