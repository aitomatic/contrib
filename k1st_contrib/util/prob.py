"""Probabilities."""


from collections import OrderedDict
from typing import Dict, OrderedDict as _OrderedDict, Sequence  # 3.9: builtins


__all__: Sequence[str] = ('ClassifProbSet', 'OrderedClassifProbSet',
                          'normalize', 'order')


ClassifProbSet: type = Dict[str, float]
OrderedClassifProbSet: type = _OrderedDict[str, float]


def normalize(d: ClassifProbSet, /) -> ClassifProbSet:
    """Normalize output probabilities."""
    return ({k: v / s for k, v in d.items()}
            if (s := sum(d.values())) > 0
            else {k: 1 / (_ := len(d)) for k in d})


def order(d: ClassifProbSet, /) -> OrderedClassifProbSet:
    """Rank output probabilities."""
    return OrderedDict(sorted(d.items(), key=lambda tup: tup[1], reverse=True))
