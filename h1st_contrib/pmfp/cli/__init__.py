"""Predictive Maintenance / Fault Prediction ("PMFP") CLI."""


import click

from .oracle import (oraclize_fault_pred_teacher,
                     predict_faults,
                     tune_fault_pred_student_decision_threshold)


__all__ = ('h1st_pmfp_cli',)


@click.group(name='pmfp',
             cls=click.Group,
             commands={'oralize-fault-pred-teacher': oraclize_fault_pred_teacher,   # noqa: E501
                       'predict-faults': predict_faults,
                       'tune-fault-pred-student-decision-threshold':
                       tune_fault_pred_student_decision_threshold},
             invoke_without_command=False,
             no_args_is_help=True,
             subcommand_metavar='H1ST_SUB_COMMAND',
             chain=False,
             help='H1st CLI >>>',
             epilog='^^^ H1st CLI',
             short_help='H1st CLI',
             options_metavar='[OPTIONS]',
             add_help_option=True,
             hidden=False,
             deprecated=False)
def h1st_pmfp_cli():
    """Predictive Maintenance / Fault Prediction ("PMFP") CLI."""
