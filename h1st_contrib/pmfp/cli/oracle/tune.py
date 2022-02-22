"""Tune a Knowledge Generalizer ("Student") model's decision threshold.

Example:
AWS_ACCESS_KEY_ID=<...aws-access-key-id...> \
AWS_SECRET_ACCESS_KEY=<...aws-secret-access-key...> \
    h1st pmfp tune-fault-pred-student-decision-threshold \
    <...student-model-version...> \
    2016-09-01 2022-02-22
"""


from typing import Tuple   # Python 3.9+: use built-ins/collections.abc

import click

from h1st_contrib.pmfp.models import TimeSeriesDLFaultPredStudent

import h1st_contrib.utils.debug


@click.command(name='tune-fault-pred-student-decision-threshold')
def tune_fault_pred_student_decision_threshold(
        student_version: str,
        date_range: Tuple[str, str],
        debug: bool = False):
    """Tune a Knowledge Generalizer ("Student") model's decision threshold."""
    if debug:
        h1st_contrib.utils.debug.ON = True

    # load Student model
    student: TimeSeriesDLFaultPredStudent = \
        TimeSeriesDLFaultPredStudent.load(version=student_version)

    # tune Student's decision threshold
    student.tune_decision_threshold(tuning_date_range=date_range)
