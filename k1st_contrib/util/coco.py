"""COCO utilities."""


import json
from tempfile import NamedTemporaryFile
from typing import Dict, List, Sequence, Tuple  # Py3.9+: built-ins/collections

from .type import Num


__all__: Sequence[str] = ('coco_with_largest_obj_per_img',)


def coco_with_largest_obj_per_img(coco_file_path: str) -> str:
    """Create a filtered COCO file with only 1 largest object per image."""
    with open(file=coco_file_path, mode='rt', encoding='utf8') as f:
        coco: dict = json.load(fp=f)

    largest_obj_of_img: Dict[int, dict] = {}

    for d in coco['annotations']:
        largest_obj: dict = largest_obj_of_img.setdefault(d['image_id'], {})

        if d['area'] > largest_obj.get('area', 0):
            largest_obj['area']: float = d['area']
            largest_obj['id'] = d['id']

    coco['annotations']: List[dict] = [i
                                       for i in coco['annotations']
                                       if i['id'] in [j['id']
                                                      for j in largest_obj_of_img.values()]]  # noqa: E501

    with NamedTemporaryFile(mode='wt', encoding='utf', delete=False) as f:
        json.dump(obj=coco, fp=f, indent=2)

    return f.name


def _bbox(bbox_0: Tuple[Num, Num, Num, Num],
          bbox_1: Tuple[Num, Num, Num, Num], /) -> Tuple[float, float, float, float]:  # noqa: E501
    return tuple(((i + j) / 2) for i, j in zip(bbox_0, bbox_1))
