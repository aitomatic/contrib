"""Image Classification utilities."""


from pathlib import Path
from typing import Dict, Sequence, Union

from numpy import ndarray
from PIL.Image import Image


__all__: Sequence[str] = 'ImgInputType', 'ImgClassifType', 'normalize'


ImgInputType: type = Union[Image, ndarray, Path, str]
ImgClassifType: type = Dict[str, float]


def normalize(d: ImgClassifType, /) -> ImgClassifType:
    """Normalize output probabilities."""
    return {k: v / (_ := sum(d.values())) for k, v in d.items()}
