from tasks.task_08_dcel_records.exercise import Vertex, make_edge
from de_berg_geometry.model import Point


def test_edge_is_two_opposite_half_edges() -> None:
    a, b = Vertex(Point(0, 0)), Vertex(Point(1, 0))
    forward, backward = make_edge(a, b)
    assert forward.origin is a
    assert forward.destination is b
    assert backward.origin is b
    assert forward.twin is backward
    assert backward.twin is forward
    assert a.incident_edge is forward
    assert b.incident_edge is backward
