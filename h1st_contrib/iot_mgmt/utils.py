"""Utilities."""


import re


__all__ = (
    'MAX_CHAR_LEN',
    'clean_lower_str', 'clean_upper_str',
)


MAX_CHAR_LEN: int = 255


def _clean_str(s: str) -> str:
    return re.sub('_{2,}', '_', re.sub(r'[^\w]+', '_', s).strip('_'))


def clean_lower_str(s: str) -> str:
    """Clean & lower-case a string."""
    return _clean_str(s).lower()


def clean_upper_str(s: str) -> str:
    """Clean & upper-case a string."""
    return _clean_str(s).upper()
