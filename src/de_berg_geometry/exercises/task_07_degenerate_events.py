from dataclasses import dataclass

from de_berg_geometry.model import Point, Segment


@dataclass(frozen=True)
class EventSets:
    upper: frozenset[str]
    lower: frozenset[str]
    containing: frozenset[str]

    @property
    def is_intersection(self) -> bool:
        raise NotImplementedError


def classify_event(point: Point, segments: list[Segment]) -> EventSets:
    raise NotImplementedError
