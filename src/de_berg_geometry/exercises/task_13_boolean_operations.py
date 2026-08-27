from enum import Enum, auto

from shapely.geometry import MultiPolygon, Polygon

from de_berg_geometry.exercises.task_12_overlay_labels import OverlayCell


class BooleanOperation(Enum):
    UNION = auto()
    INTERSECTION = auto()
    DIFFERENCE = auto()
    XOR = auto()


def select_cells(
    cells: list[OverlayCell], operation: BooleanOperation, layer_a: str, layer_b: str
) -> Polygon | MultiPolygon:
    raise NotImplementedError
