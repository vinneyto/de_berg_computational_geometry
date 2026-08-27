from de_berg_geometry.model import EPSILON, Point


def cross(a: Point, b: Point, c: Point) -> float:
    """Return the signed area multiplier for triangle ABC."""
    raise NotImplementedError


def orientation(a: Point, b: Point, c: Point, eps: float = EPSILON) -> int:
    """Return 1 for left, -1 for right, and 0 for collinear."""
    raise NotImplementedError


def point_on_segment(point: Point, start: Point, end: Point, eps: float = EPSILON) -> bool:
    raise NotImplementedError
