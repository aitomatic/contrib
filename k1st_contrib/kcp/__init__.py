"""Knowledge-Conditioned Probabilities (k-CP)."""


from typing import Sequence, Union

from ..util.prob import normalize
from ..util.types import ClassifType


class KCP:  # pylint: disable=too-few-public-methods
    """Knowledge-Conditioned Probabilities (k-CP)."""

    def __init__(self, k_contrib: float = 0.68):
        """Initialize."""
        self.k_contrib: float = k_contrib
        self.ml_contrib: float = 1 - k_contrib

    def __call__(self,
                 k_classif: Union[ClassifType, Sequence[ClassifType]],
                 ml_classif: Union[ClassifType, Sequence[ClassifType]]) \
            -> Union[ClassifType, Sequence[ClassifType]]:
        """Fuse 2 sets of probabilities."""
        if isinstance(k_classif, (list, tuple)):
            assert (isinstance(ml_classif, (list, tuple)) and
                    (len(ml_classif) == (n := len(k_classif)))), \
                f'*** ml_classif NOT A SEQUENCE OF LENGTH {n} ***'

            return [{class_name: (self.k_contrib * k_prob +
                                  self.ml_contrib * d1[class_name])
                    for class_name, k_prob in d0.items()}
                    for d0, d1 in zip(k_classif, ml_classif)]

        return {class_name: (self.k_contrib * k_prob +
                             self.ml_contrib * ml_classif[class_name])
                for class_name, k_prob in k_classif.items()}
