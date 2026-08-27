from dataclasses import dataclass

from shapely.geometry import Polygon


@dataclass(frozen=True)
class LabeledPolygon:
    polygon: Polygon
    layer: str
    label: str


@dataclass(frozen=True)
class OverlayCell:
    polygon: Polygon
    labels: tuple[tuple[str, str], ...]

    def label_map(self) -> dict[str, str]:
        return dict(self.labels)


def build_labeled_overlay(inputs: list[LabeledPolygon]) -> list[OverlayCell]:
    raise NotImplementedError
