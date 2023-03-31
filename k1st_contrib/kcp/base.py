"""Knowledge-Conditioned Probabilities (k-CP)."""


from math import prod
from typing import Sequence, Union

from ..util.prob import ClassifProbSet, normalize


class KCP:  # pylint: disable=too-few-public-methods
    """Knowledge-Conditioned Probabilities (k-CP)."""

    def __call__(
            self,
            classif_0: Union[ClassifProbSet, Sequence[ClassifProbSet]], /,
            *other_classifs: Union[ClassifProbSet, Sequence[ClassifProbSet]]) \
            -> Union[ClassifProbSet, Sequence[ClassifProbSet]]:
        """Fuse multiple sets of probabilities."""
        if isinstance(classif_0, (list, tuple)):
            assert (n := len(classif_0)) > 0

            for classif in other_classifs:
                assert (isinstance(classif, (list, tuple)) and
                        (len(classif) == n)), \
                    f'*** {classif} NOT A SEQUENCE OF LENGTH {n} ***'

            return [normalize({class_name: prod(classif[class_name]
                                                for classif in classifs)
                               for class_name in classif_0})
                    for classifs in zip(classif_0, *other_classifs)]

        return normalize({class_name: prod(classif[class_name]
                                           for classif in (classif_0, *other_classifs))  # noqa:E501
                          for class_name in classif_0})
