"""Type utilities."""


from collections.abc import Sequence
from typing import Union


__all__: Sequence[str] = ('Num',)


Num: type = Union[float, int]
