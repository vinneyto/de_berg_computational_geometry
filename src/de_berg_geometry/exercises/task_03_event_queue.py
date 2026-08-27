from dataclasses import dataclass, field
from enum import Enum, auto

from de_berg_geometry.model import Point


class EventKind(Enum):
    UPPER = auto()
    INTERSECTION = auto()
    LOWER = auto()


@dataclass
class Event:
    point: Point
    kinds: set[EventKind] = field(default_factory=set)
    segment_names: set[str] = field(default_factory=set)


class EventQueue:
    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, point: Point, kind: EventKind, segment_names: set[str]) -> None:
        raise NotImplementedError

    def pop(self) -> Event:
        raise NotImplementedError

    def __bool__(self) -> bool:
        raise NotImplementedError
