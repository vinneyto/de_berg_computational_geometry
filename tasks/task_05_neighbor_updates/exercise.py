Pair = tuple[str, str]


def canonical_pair(first: str, second: str) -> Pair:
    raise NotImplementedError


def adjacent_pairs(order: list[str]) -> set[Pair]:
    raise NotImplementedError


def newly_adjacent(before: list[str], after: list[str]) -> set[Pair]:
    """Return pairs adjacent after the event but not before it."""
    raise NotImplementedError
