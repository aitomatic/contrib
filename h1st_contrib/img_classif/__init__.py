"""Image Classification."""


from typing import Sequence

from .imagenet_classifier import imagenet_classify


__all__: Sequence[str] = (
    'imagenet_classify',
)
