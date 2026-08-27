from sortedcontainers import SortedList

from de_berg_geometry.model import Segment


def x_at(segment: Segment, y: float) -> float:
    raise NotImplementedError


class SweepStatus:
    def __init__(self, y: float) -> None:
        self.y = y
        self._segments: SortedList[Segment] = SortedList(key=self._key)

    def _key(self, segment: Segment) -> tuple[float, str]:
        return x_at(segment, self.y), segment.name

    def set_y(self, y: float) -> None:
        raise NotImplementedError

    def add(self, segment: Segment) -> None:
        raise NotImplementedError

    def remove(self, segment: Segment) -> None:
        raise NotImplementedError

    def neighbors(self, segment: Segment) -> tuple[Segment | None, Segment | None]:
        raise NotImplementedError

    def names(self) -> list[str]:
        return [segment.name for segment in self._segments]
