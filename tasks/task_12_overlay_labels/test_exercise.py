import pytest
from shapely.geometry import box

from tasks.task_12_overlay_labels.exercise import LabeledPolygon, build_labeled_overlay


def test_overlap_is_split_into_labeled_cells() -> None:
    inputs = [
        LabeledPolygon(box(0, 0, 2, 2), "map_a", "inside_a"),
        LabeledPolygon(box(1, 0, 3, 2), "map_b", "inside_b"),
    ]
    cells = build_labeled_overlay(inputs)
    areas = {tuple(sorted(cell.labels)): cell.polygon.area for cell in cells}
    assert areas[(('map_a', 'inside_a'),)] == pytest.approx(2)
    assert areas[(('map_b', 'inside_b'),)] == pytest.approx(2)
    assert areas[(('map_a', 'inside_a'), ('map_b', 'inside_b'))] == pytest.approx(2)
