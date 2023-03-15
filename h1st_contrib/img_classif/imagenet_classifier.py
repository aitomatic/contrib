"""ImageNet Classifier."""


import json
from pathlib import Path
from typing import Sequence, Set, Union

from transformers.pipelines import pipeline
from transformers.pipelines.image_classification import \
    ImageClassificationPipeline

from .util import ImgInputType, ImgClassifType


__all__: Sequence[str] = ('imagenet_classify',)


IMAGENET_CLASSES_FILE_NAME: str = 'ImageNet-Classes.json'
IMAGENET_N_CLASSES: int = 10 ** 3 - 3  # duplicates: cardigan, crane, maillot

with open(file=Path(__file__).parent / IMAGENET_CLASSES_FILE_NAME,
          mode='rt', encoding='utf8') as f:
    IMAGENET_CLASSES: Set[str] = {v[1].lower() for k, v in json.load(f).items()}  # noqa: E501
    assert len(IMAGENET_CLASSES) == IMAGENET_N_CLASSES


IMAGENET_CLASSIFIER: ImageClassificationPipeline = \
    pipeline(task='image-classification',
             model=None,
             config=None,
             tokenizer=None,
             feature_extractor=None,
             framework=None,
             revision=None,
             use_fast=True,
             use_auth_token=None,
             device=None,
             device_map=None,
             torch_dtype=None,
             trust_remote_code=None,
             model_kwargs={},
             pipeline_class=None)


def imagenet_classify(
        img_input: Union[ImgInputType, Sequence[ImgInputType]], /) \
        -> Union[ImgClassifType, Sequence[ImgClassifType]]:
    """Classify image(s) according to ImageNet."""
    if isinstance(img_input, (list, tuple)):
        return [imagenet_classify(i) for i in img_input]

    imagenet_classif: ImgClassifType = {
        i['label'].split(',')[0].replace(' ', '_').lower(): i['score']
        for i in IMAGENET_CLASSIFIER(img_input, top_k=IMAGENET_N_CLASSES)
    }

    assert IMAGENET_CLASSES.issuperset(imagenet_classif), \
        KeyError('*** INVALID OUTPUT CLASSES '
                 f'{set(imagenet_classif).difference(IMAGENET_CLASSES)} ***')

    return imagenet_classif
