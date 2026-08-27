from tasks.task_01_predicates.exercise import orientation, point_on_segment
from de_berg_geometry.model import Point


def test_orientation_distinguishes_left_right_and_collinear() -> None:
    a, b = Point(0, 0), Point(2, 0)
    assert orientation(a, b, Point(1, 1)) == 1
    assert orientation(a, b, Point(1, -1)) == -1
    assert orientation(a, b, Point(1, 0)) == 0


def test_point_on_segment_rejects_collinear_point_outside_bounds() -> None:
    a, b = Point(0, 0), Point(2, 0)
    assert point_on_segment(Point(1, 0), a, b)
    assert point_on_segment(a, a, b)
    assert not point_on_segment(Point(3, 0), a, b)
    assert not point_on_segment(Point(1, 0.1), a, b)
