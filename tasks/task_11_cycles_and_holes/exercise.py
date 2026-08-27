from dataclasses import dataclass

from de_berg_geometry.model import Point


@dataclass(frozen=True)
class RegionCycles:
    outer: tuple[Point, ...]
    holes: tuple[tuple[Point, ...], ...]


def signed_area(cycle: list[Point] | tuple[Point, ...]) -> float:
    raise NotImplementedError


def group_cycles(cycles: list[list[Point]]) -> list[RegionCycles]:
    """Attach every clockwise hole to the smallest containing CCW cycle."""
    raise NotImplementedError
