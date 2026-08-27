from de_berg_geometry.exercises.task_03_event_queue import EventKind, EventQueue
from de_berg_geometry.model import Point


def test_events_are_processed_top_to_bottom_then_left_to_right() -> None:
    queue = EventQueue()
    queue.push(Point(3, 2), EventKind.UPPER, {"a"})
    queue.push(Point(2, 3), EventKind.UPPER, {"b"})
    queue.push(Point(1, 3), EventKind.UPPER, {"c"})
    assert [queue.pop().point for _ in range(3)] == [Point(1, 3), Point(2, 3), Point(3, 2)]


def test_same_point_is_merged() -> None:
    queue = EventQueue()
    point = Point(1, 1)
    queue.push(point, EventKind.UPPER, {"a"})
    queue.push(point, EventKind.INTERSECTION, {"a", "b"})
    event = queue.pop()
    assert event.kinds == {EventKind.UPPER, EventKind.INTERSECTION}
    assert event.segment_names == {"a", "b"}
    assert not queue
