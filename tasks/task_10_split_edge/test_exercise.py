from tasks.task_09_dcel_traversal.exercise import make_polygon, walk_boundary
from tasks.task_10_split_edge.exercise import split_edge
from de_berg_geometry.model import Point


def test_split_preserves_both_face_cycles_and_twins() -> None:
    _, inside, outside = make_polygon([Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)])
    old = inside.outer_component
    assert old is not None
    result = split_edge(old, Point(1, 0))
    inside_edges = walk_boundary(result.first)
    outside_edges = walk_boundary(result.first.twin)  # type: ignore[arg-type]
    assert len(inside_edges) == 5
    assert len(outside_edges) == 5
    assert result.first.destination is result.vertex
    assert result.second.origin is result.vertex
    assert all(edge.twin.twin is edge for edge in inside_edges + outside_edges)  # type: ignore[union-attr]
