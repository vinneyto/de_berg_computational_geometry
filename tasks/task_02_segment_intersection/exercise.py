from dataclasses import dataclass
from enum import Enum, auto

from de_berg_geometry.model import Point, Segment


class IntersectionKind(Enum):
    NONE = auto()
    POINT = auto()
    OVERLAP = auto()


@dataclass(frozen=True)
class Intersection:
    kind: IntersectionKind
    point: Point | None = None


def segment_intersection(first: Segment, second: Segment) -> Intersection:
    raise NotImplementedError
