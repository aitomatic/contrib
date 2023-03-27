"""Knowledge-Conditioned Probabilities for Computer Vision (k-CPCV)."""


from typing import Sequence, Union

from ..util.prob import normalize
from ..util.types import ClassifType


class KCPCV:  # pylint: disable=too-few-public-methods
    """Knowledge-Conditioned Probabilities (k-CP)."""

    def __call__(self,
                 k_classif: Union[ClassifType, Sequence[ClassifType]],
                 ml_classif: Union[ClassifType, Sequence[ClassifType]]) \
            -> Union[ClassifType, Sequence[ClassifType]]:
        """Fuse multiple sets of probabilities."""
        if isinstance(k_classif, (list, tuple)):
            assert (isinstance(ml_classif, (list, tuple)) and
                    (len(ml_classif) == (n := len(k_classif)))), \
                f'*** ml_classif NOT A SEQUENCE OF LENGTH {n} ***'

            return [normalize({class_name: (k_prob * d1[class_name])
                               for class_name, k_prob in d0.items()})
                    for d0, d1 in zip(k_classif, ml_classif)]

        return normalize({class_name: (k_prob * ml_classif[class_name])
                          for class_name, k_prob in k_classif.items()})
