from de_berg_geometry.exercises.task_09_dcel_traversal import (
    boundary_points,
    make_polygon,
    outgoing_edges,
    walk_boundary,
)
from de_berg_geometry.model import Point


def test_walk_boundary_returns_one_closed_cycle() -> None:
    vertices, inside, _ = make_polygon([Point(0, 0), Point(2, 0), Point(1, 1)])
    assert len(walk_boundary(inside.outer_component)) == 3  # type: ignore[arg-type]
    assert boundary_points(inside) == [Point(0, 0), Point(2, 0), Point(1, 1)]
    assert len(outgoing_edges(vertices[0])) == 2
