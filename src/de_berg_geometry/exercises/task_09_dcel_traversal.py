from de_berg_geometry.exercises.task_08_dcel_records import Face, HalfEdge, Vertex, make_edge
from de_berg_geometry.model import Point


def make_polygon(points: list[Point]) -> tuple[list[Vertex], Face, Face]:
    """Provided scaffold: create CCW inner boundary and its unbounded twin boundary."""
    vertices = [Vertex(point) for point in points]
    pairs = [
        make_edge(vertices[i], vertices[(i + 1) % len(vertices)])
        for i in range(len(vertices))
    ]
    inside, outside = Face("inside"), Face("outside")
    forward = [pair[0] for pair in pairs]
    backward = [pair[1] for pair in pairs]
    for i, edge in enumerate(forward):
        edge.next = forward[(i + 1) % len(forward)]
        edge.prev = forward[(i - 1) % len(forward)]
        edge.face = inside
    reversed_back = list(reversed(backward))
    for i, edge in enumerate(reversed_back):
        edge.next = reversed_back[(i + 1) % len(reversed_back)]
        edge.prev = reversed_back[(i - 1) % len(reversed_back)]
        edge.face = outside
    inside.outer_component = forward[0]
    outside.inner_components = [reversed_back[0]]
    return vertices, inside, outside


def walk_boundary(start: HalfEdge, max_steps: int = 10_000) -> list[HalfEdge]:
    raise NotImplementedError


def boundary_points(face: Face) -> list[Point]:
    raise NotImplementedError


def outgoing_edges(vertex: Vertex, max_steps: int = 10_000) -> list[HalfEdge]:
    raise NotImplementedError
