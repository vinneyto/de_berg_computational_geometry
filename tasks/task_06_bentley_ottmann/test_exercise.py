from tasks.task_06_bentley_ottmann.exercise import find_intersections
from de_berg_geometry.model import Point, Segment


def test_sweep_finds_chain_of_revealed_intersections() -> None:
    segments = [
        Segment(Point(0, 4), Point(4, 0), "a"),
        Segment(Point(4, 4), Point(0, 0), "b"),
        Segment(Point(3, 4), Point(3, 0), "c"),
    ]
    result = find_intersections(segments)
    assert set(result.points) == {Point(2, 2), Point(3, 1), Point(3, 3)}


def test_sparse_scene_avoids_quadratic_pair_checks() -> None:
    segments = [Segment(Point(x, 2), Point(x + 0.1, 0), str(x)) for x in range(20)]
    result = find_intersections(segments)
    assert result.points == ()
    assert result.tested_pairs < 20 * 19 // 2
