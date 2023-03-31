"""Probabilities."""


from typing import Dict, List, Sequence, Tuple  # Py3.9+: use built-ins


__all__: Sequence[str] = 'ClassifProbSet', 'normalize', 'rank'


ClassifProbSet: type = Dict[str, float]


def normalize(d: ClassifProbSet, /) -> ClassifProbSet:
    """Normalize output probabilities."""
    return ({k: v / s for k, v in d.items()}
            if (s := sum(d.values())) > 0
            else {k: 1 / (_ := len(d)) for k in d})


def rank(d: ClassifProbSet, /) -> List[Tuple[str, float]]:
    """Rank output probabilities."""
    return sorted(d.items(), key=lambda tup: tup[1], reverse=True)
