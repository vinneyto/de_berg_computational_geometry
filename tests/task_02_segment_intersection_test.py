from de_berg_geometry.exercises.task_02_segment_intersection import (
    IntersectionKind,
    segment_intersection,
)
from de_berg_geometry.model import Point, Segment


def segment(a: tuple[float, float], b: tuple[float, float]) -> Segment:
    return Segment(Point(*a), Point(*b))


def test_proper_crossing_returns_point() -> None:
    result = segment_intersection(segment((0, 0), (2, 2)), segment((0, 2), (2, 0)))
    assert result.kind is IntersectionKind.POINT
    assert result.point == Point(1, 1)


def test_endpoint_touch_is_an_intersection() -> None:
    result = segment_intersection(segment((0, 0), (1, 1)), segment((1, 1), (2, 0)))
    assert result == type(result)(IntersectionKind.POINT, Point(1, 1))


def test_disjoint_and_overlap_are_distinguished() -> None:
    disjoint = segment_intersection(segment((0, 0), (1, 0)), segment((2, 0), (3, 0)))
    overlap = segment_intersection(segment((0, 0), (2, 0)), segment((1, 0), (3, 0)))
    assert disjoint.kind is IntersectionKind.NONE
    assert overlap.kind is IntersectionKind.OVERLAP
