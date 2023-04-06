"""Type utilities."""


from typing import Sequence, Union  # Py3.9+: use built-ins/collections.abc


__all__: Sequence[str] = ('Num',)


Num: type = Union[float, int]
