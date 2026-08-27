from tasks.task_05_neighbor_updates.exercise import adjacent_pairs, newly_adjacent


def test_adjacent_pairs_does_not_generate_all_pairs() -> None:
    assert adjacent_pairs(["a", "b", "c", "d"]) == {("a", "b"), ("b", "c"), ("c", "d")}


def test_removal_creates_one_new_candidate() -> None:
    assert newly_adjacent(["a", "b", "c"], ["a", "c"]) == {("a", "c")}


def test_crossing_creates_only_external_candidates() -> None:
    assert newly_adjacent(["a", "b", "c", "d"], ["a", "c", "b", "d"]) == {
        ("a", "c"),
        ("b", "d"),
    }
