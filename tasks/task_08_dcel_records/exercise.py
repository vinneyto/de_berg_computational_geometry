from dataclasses import dataclass, field

from de_berg_geometry.model import Point


@dataclass(eq=False)
class Vertex:
    point: Point
    incident_edge: "HalfEdge | None" = None


@dataclass(eq=False)
class Face:
    name: str
    outer_component: "HalfEdge | None" = None
    inner_components: list["HalfEdge"] = field(default_factory=list)


@dataclass(eq=False)
class HalfEdge:
    origin: Vertex
    twin: "HalfEdge | None" = None
    next: "HalfEdge | None" = None
    prev: "HalfEdge | None" = None
    face: Face | None = None

    @property
    def destination(self) -> Vertex:
        raise NotImplementedError


def make_edge(origin: Vertex, destination: Vertex) -> tuple[HalfEdge, HalfEdge]:
    raise NotImplementedError
