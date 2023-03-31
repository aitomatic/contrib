"""Image Classification utilities."""


from pathlib import Path
from typing import Sequence, Union

from PIL.Image import Image


__all__: Sequence[str] = ('ImgInput',)


ImgInput: type = Union[Image, Path, str]
