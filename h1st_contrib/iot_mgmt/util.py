"""Utilities."""


import re
import sys

if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = (
    'MAX_CHAR_LEN',
    'clean_lower_str', 'clean_upper_str',
)


# pylint: disable=invalid-name


MAX_CHAR_LEN = 255


def _clean_str(s: str) -> str:
    return re.sub('_{2,}', '_', re.sub(r'[^\w]+', '_', s).strip('_'))


def clean_lower_str(s: str) -> str:
    """Clean & lower-case a string."""
    return _clean_str(s).lower()


def clean_upper_str(s: str) -> str:
    """Clean & upper-case a string."""
    return _clean_str(s).upper()
