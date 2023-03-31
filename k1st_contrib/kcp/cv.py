"""Knowledge-Conditioned Probabilities for Computer Vision (k-CPCV)."""


from typing import Sequence, Union

from ..util.prob import ClassifProbSet
from .base import KCP


class KCPCV(KCP):  # pylint: disable=too-few-public-methods
    """Knowledge-Conditioned Probabilities for Computer Vision (k-CPCV)."""

    def __call__(self, *args, **kwargs) \
            -> Union[ClassifProbSet, Sequence[ClassifProbSet]]:
        """Classify image(s)."""
