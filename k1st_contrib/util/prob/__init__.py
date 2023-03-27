"""Probabilities."""


from typing import Sequence

from k1st_contrib.util.types import ClassifType


__all__: Sequence[str] = ('normalize',)


def normalize(d: ClassifType, /) -> ClassifType:
    """Normalize output probabilities."""
    return ({k: v / s for k, v in d.items()}
            if (s := sum(d.values())) > 0
            else {k: 1 / (_ := len(d)) for k in d})
