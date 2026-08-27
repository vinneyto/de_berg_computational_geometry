from dataclasses import dataclass

EPSILON = 1e-9


@dataclass(frozen=True, order=True)
class Point:
    x: float
    y: float


@dataclass(frozen=True)
class Segment:
    start: Point
    end: Point
    name: str = ""

    @property
    def upper(self) -> Point:
        return min((self.start, self.end), key=lambda point: (-point.y, point.x))

    @property
    def lower(self) -> Point:
        return max((self.start, self.end), key=lambda point: (-point.y, point.x))
