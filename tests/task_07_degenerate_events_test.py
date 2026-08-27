from de_berg_geometry.exercises.task_07_degenerate_events import classify_event
from de_berg_geometry.model import Point, Segment


def test_common_point_is_partitioned_into_u_l_c() -> None:
    p = Point(1, 1)
    segments = [
        Segment(p, Point(0, 0), "starts"),
        Segment(Point(0, 2), p, "ends"),
        Segment(Point(1, 2), Point(1, 0), "passes"),
        Segment(Point(-1, 1), Point(2, 1), "horizontal"),
    ]
    groups = classify_event(p, segments)
    assert groups.upper == frozenset({"starts"})
    assert groups.lower == frozenset({"ends"})
    assert groups.containing == frozenset({"passes", "horizontal"})
    assert groups.is_intersection


def test_single_endpoint_is_not_intersection() -> None:
    segment = Segment(Point(0, 1), Point(0, 0), "only")
    assert not classify_event(Point(0, 1), [segment]).is_intersection
