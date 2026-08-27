from dataclasses import dataclass

from de_berg_geometry.model import Point, Segment


@dataclass(frozen=True)
class SweepResult:
    points: tuple[Point, ...]
    tested_pairs: int


def find_intersections(segments: list[Segment]) -> SweepResult:
    """Find intersections with a sweep; input is in general position."""
    raise NotImplementedError
