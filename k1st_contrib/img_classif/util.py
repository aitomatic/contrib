"""Image Classification utilities."""


from pathlib import Path
from typing import Sequence, Union

from PIL.Image import Image

from ..util.types import ClassifType


__all__: Sequence[str] = 'ImgInputType', 'ImgClassifType'


ImgInputType: type = Union[Image, Path, str]
ImgClassifType: type = ClassifType
