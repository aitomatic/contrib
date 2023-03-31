"""ImageNet Classifier."""


import json
from pathlib import Path
from typing import Dict, List, Sequence, Set, Tuple  # Py3.9+: use built-ins
from typing import Union

from transformers.pipelines import pipeline
from transformers.pipelines.image_classification import ImageClassificationPipeline  # noqa: E501

from ..util.prob import ClassifProbSet, normalize, rank
from .util import ImgInput


__all__: Sequence[str] = (
    'imagenet_classify',
    'ImageNetSimilarityBasedClassifier',
)


IMAGENET_CLASSES_FILE_NAME: str = 'ImageNet-Classes.json'
IMAGENET_N_CLASSES: int = 10 ** 3 - 3  # duplicates: cardigan, crane, maillot

with open(file=Path(__file__).parent / IMAGENET_CLASSES_FILE_NAME,
          mode='rt', encoding='utf8') as f:
    IMAGENET_CLASSES: Set[str] = {v[1].lower() for v in json.load(f).values()}
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


def imagenet_classify(img_input: Union[ImgInput, Sequence[ImgInput]], /) \
        -> Union[ClassifProbSet, Sequence[ClassifProbSet]]:
    """Classify image(s) according to ImageNet."""
    if isinstance(img_input, (list, tuple)):
        return [imagenet_classify(i) for i in img_input]

    imagenet_classif: ClassifProbSet = {
        i['label'].split(',')[0].replace(' ', '_').lower(): i['score']
        for i in IMAGENET_CLASSIFIER(img_input, top_k=IMAGENET_N_CLASSES)
    }

    assert IMAGENET_CLASSES.issuperset(imagenet_classif), \
        KeyError('*** INVALID OUTPUT CLASSES '
                 f'{set(imagenet_classif).difference(IMAGENET_CLASSES)} ***')

    return imagenet_classif


def profile_imagenet_similarity(imgs: Sequence[ImgInput],
                                labels: Sequence[str]) \
        -> Dict[str, List[Tuple[str, float]]]:
    """Profile similarity between ImageNet classes a set of labels."""
    imagenet_classifs: Sequence[ClassifProbSet] = imagenet_classify(imgs)

    d: Dict[str, Dict[str, float]] = {}

    for imagenet_classif, label in zip(imagenet_classifs, labels):
        profile: Dict[str, float] = d.setdefault(label, {})

        for imagenet_class_name, prob in imagenet_classif.items():
            if imagenet_class_name in profile:
                profile[imagenet_class_name] += prob
            else:
                profile[imagenet_class_name]: float = prob

    return {k: rank(normalize(v)) for k, v in d.items()}


class ImageNetSimilarityBasedClassifier:
    # pylint: disable=too-few-public-methods
    """Classify target classes based on mapping from such classes to ImageNet."""  # noqa: E501

    def __init__(
            self,
            classes_mapped_to_similar_imagenet_classes: Dict[str, List[str]],
            /, *, prob_threshold: float = 3e-6):
        """Initialize."""
        self.classes_mapped_to_imagenet_classes: Dict[str, List[str]] = \
            classes_mapped_to_similar_imagenet_classes

        self.prob_threshold: float = prob_threshold

    def __call__(self,
                 img_input: Union[ImgInput, Sequence[ImgInput]]) \
            -> Union[ClassifProbSet, Sequence[ClassifProbSet]]:
        """Classify."""
        return (
            [normalize({
                target_class:
                sum((p
                     if (p := i.get(imagenet_class, 0)) > self.prob_threshold
                     else 0)
                    for imagenet_class in imagenet_classes)
                for target_class, imagenet_classes
                in self.classes_mapped_to_imagenet_classes.items()})
             for i in imagenet_classif]

            if isinstance(imagenet_classif := imagenet_classify(img_input),
                          (list, tuple))

            else normalize(
                {target_class:
                 sum((p
                      if ((p := imagenet_classif.get(imagenet_class, 0))
                          > self.prob_threshold)
                      else 0)
                     for imagenet_class in imagenet_class_names)
                 for target_class, imagenet_class_names
                 in self.classes_mapped_to_imagenet_classes.items()})
        )
