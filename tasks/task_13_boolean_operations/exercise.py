from enum import Enum, auto

from shapely.geometry import MultiPolygon, Polygon

from tasks.task_12_overlay_labels.exercise import OverlayCell


class BooleanOperation(Enum):
    UNION = auto()
    INTERSECTION = auto()
    DIFFERENCE = auto()
    XOR = auto()


def select_cells(
    cells: list[OverlayCell], operation: BooleanOperation, layer_a: str, layer_b: str
) -> Polygon | MultiPolygon:
    raise NotImplementedError
