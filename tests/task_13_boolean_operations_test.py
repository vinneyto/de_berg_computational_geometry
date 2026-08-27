import pytest
from shapely.geometry import box

from de_berg_geometry.exercises.task_12_overlay_labels import LabeledPolygon, build_labeled_overlay
from de_berg_geometry.exercises.task_13_boolean_operations import BooleanOperation, select_cells


@pytest.fixture
def overlay():
    return build_labeled_overlay(
        [LabeledPolygon(box(0, 0, 2, 2), "a", "yes"), LabeledPolygon(box(1, 0, 3, 2), "b", "yes")]
    )


@pytest.mark.parametrize(
    ("operation", "expected_area"),
    [
        (BooleanOperation.UNION, 6),
        (BooleanOperation.INTERSECTION, 2),
        (BooleanOperation.DIFFERENCE, 2),
        (BooleanOperation.XOR, 4),
    ],
)
def test_boolean_operations_are_cell_filters(overlay, operation, expected_area: float) -> None:
    assert select_cells(overlay, operation, "a", "b").area == pytest.approx(expected_area)
