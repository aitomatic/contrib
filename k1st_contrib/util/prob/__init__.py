"""Probabilities."""


from typing import Dict, Sequence  # Py3.9+: use built-ins/collections.abc


__all__: Sequence[str] = 'ClassifProbSet', 'normalize'


ClassifProbSet: type = Dict[str, float]


def normalize(d: ClassifProbSet, /) -> ClassifProbSet:
    """Normalize output probabilities."""
    return ({k: v / s for k, v in d.items()}
            if (s := sum(d.values())) > 0
            else {k: 1 / (_ := len(d)) for k in d})
