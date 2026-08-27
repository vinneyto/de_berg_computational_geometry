from dataclasses import dataclass

from tasks.task_08_dcel_records.exercise import HalfEdge, Vertex
from de_berg_geometry.model import Point


@dataclass(frozen=True)
class SplitResult:
    vertex: Vertex
    first: HalfEdge
    second: HalfEdge


def split_edge(edge: HalfEdge, point: Point) -> SplitResult:
    """Replace edge and its twin in both boundary cycles."""
    raise NotImplementedError
