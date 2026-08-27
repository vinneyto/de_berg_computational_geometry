from importlib import import_module
from pathlib import Path


def test_every_task_is_self_contained_and_documents_its_test_command() -> None:
    root = Path(__file__).parents[1]
    tasks = sorted((root / "tasks").glob("task_[0-9][0-9]_*"))

    assert len(tasks) == 13

    for task in tasks:
        readme = task / "README.md"
        exercise = task / "exercise.py"
        test = task / "test_exercise.py"

        assert readme.is_file()
        assert exercise.is_file()
        assert test.is_file()
        import_module(f"tasks.{task.name}.exercise")

        expected_command = f"uv run pytest tasks/{task.name}/test_exercise.py"
        assert expected_command in readme.read_text()
