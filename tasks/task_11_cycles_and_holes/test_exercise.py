from de_berg_geometry.model import Point
from tasks.task_11_cycles_and_holes.exercise import group_cycles, signed_area


def test_signed_area_encodes_orientation() -> None:
    ccw = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
    assert signed_area(ccw) == 4
    assert signed_area(list(reversed(ccw))) == -4


def test_hole_is_attached_to_smallest_containing_outer_cycle() -> None:
    outer = [Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4)]
    island = [Point(1, 1), Point(3, 1), Point(3, 3), Point(1, 3)]
    hole = list(reversed([Point(1.5, 1.5), Point(2, 1.5), Point(2, 2), Point(1.5, 2)]))
    regions = group_cycles([outer, island, hole])
    by_outer = {region.outer: region for region in regions}
    assert by_outer[tuple(island)].holes == (tuple(hole),)
    assert by_outer[tuple(outer)].holes == ()
