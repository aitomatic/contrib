"""Image Classification utilities."""


from pathlib import Path
from typing import Dict, Sequence, Union

from numpy import ndarray
from PIL.Image import Image


__all__: Sequence[str] = 'ImgInputType', 'ImgClassifType'


ImgInputType: type = Union[Image, ndarray, Path, str]
ImgClassifType: type = Dict[str, float]
