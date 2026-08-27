import pytest

from tasks.task_04_sweep_status.exercise import SweepStatus, x_at
from de_berg_geometry.model import Point, Segment


def test_x_at_interpolates_segment() -> None:
    assert x_at(Segment(Point(0, 0), Point(4, 2)), 1) == pytest.approx(2)


def test_order_changes_after_crossing_and_neighbors_follow_order() -> None:
    rising = Segment(Point(0, 0), Point(2, 2), "rising")
    falling = Segment(Point(2, 0), Point(0, 2), "falling")
    right = Segment(Point(3, 0), Point(3, 2), "right")
    status = SweepStatus(1.5)
    for item in (rising, falling, right):
        status.add(item)
    assert status.names() == ["falling", "rising", "right"]
    assert status.neighbors(rising) == (falling, right)
    status.set_y(0.5)
    assert status.names() == ["rising", "falling", "right"]
