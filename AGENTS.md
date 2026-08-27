# Repository guidelines

- Use `uv` for dependency management and command execution.
- Keep every lesson independently runnable with
  `uv run pytest tasks/task_XX_name/test_exercise.py`.
- Each lesson must be self-contained in `tasks/task_XX_name/` with `README.md`, `HINT.md`,
  `exercise.py`, and `test_exercise.py`.
- Expand every abbreviation on first use in lesson and hint text.
- Do not make a lesson depend on the learner having completed a later lesson.
- Prefer small geometric examples whose expected result can be checked by hand.
- Exercise modules may contain `NotImplementedError`; the corresponding lesson tests are expected
  to fail until the learner completes the task.
- Keep the infrastructure test passing even while exercise tests are incomplete.
