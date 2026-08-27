from importlib import import_module
from pathlib import Path


def test_all_lessons_have_an_exercise_and_a_test() -> None:
    root = Path(__file__).parents[1]
    lessons = sorted((root / "lessons").glob("[0-9][0-9]_*.md"))

    assert len(lessons) == 13

    for lesson in lessons:
        task = lesson.stem
        import_module(f"de_berg_geometry.exercises.task_{task}")
        assert (root / "tests" / f"task_{task}_test.py").is_file()
