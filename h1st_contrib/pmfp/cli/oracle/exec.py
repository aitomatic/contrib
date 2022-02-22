"""Batch-predict equipment faults.

Example:
AWS_ACCESS_KEY_ID=<...aws-access-key-id...> \
AWS_SECRET_ACCESS_KEY=<...aws-secret-access-key...> \
    h1st pmfp predict-faults \
    <...model-class-name...> \
    <...model-version...> \
    --from-date 2016-09-01 --to-date 2022-02-22
"""


from pprint import pprint
from typing import Optional

import click
from pandas import Series

from h1st_contrib.pmfp.models import BaseFaultPredictor, H1ST_BATCH_OUTPUT_S3_DIR_PATH  # noqa: E501

import h1st_contrib.utils.debug


@click.command(name='predict-faults',
               cls=click.Command)
def predict_faults(
        model_class_name: str, model_version: str,
        date: str, to_date: Optional[str] = None,
        debug: bool = False):
    """Batch-predict equipment faults."""
    if debug:
        h1st_contrib.utils.debug.ON = True

    # load model
    import ai.models   # pylint: disable=import-error,import-outside-toplevel

    model: BaseFaultPredictor = (getattr(ai.models, model_class_name)
                                 .load(version=model_version))

    # predict
    results: Series = model.batch_process(date=date, to_date=to_date,
                                          return_json=False)

    # filter for positive predictions
    fault_preds: Series = results.loc[(results.map(sum) > 0)
                                      if isinstance(results.iloc[0], tuple)
                                      else results]

    # print
    pprint(fault_preds.to_dict())

    # save
    fault_preds.to_csv(
        output_path := (f'{H1ST_BATCH_OUTPUT_S3_DIR_PATH}/'
                        f'{model_class_name}/{model_version}/'
                        f'{date}-to-{to_date}.csv'),
        header=True, index=True)
    print(f'\n@ {output_path}')

    # summarize
    print(f'\n{(n_faults := len(fault_preds)):,} Predicted Daily Faults '
          f'({100 * n_faults / (n := len(results)):.3f}% of {n:,})')
