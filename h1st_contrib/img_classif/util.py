"""Image Classification utilities."""


from pathlib import Path
from typing import Dict, Sequence, Union

from PIL.Image import Image


__all__: Sequence[str] = (
    'ImgInputType',
    'ImgClassifType',
)


ImgInputType: type = Union[Image, Path, str]
ImgClassifType: type = Dict[str, float]
