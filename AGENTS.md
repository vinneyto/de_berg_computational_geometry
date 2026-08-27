# Repository guidelines

- Use `uv` for dependency management and command execution.
- Keep every lesson independently runnable with `uv run pytest tests/task_XX_*.py`.
- Each new lesson must contain a concept page in `lessons/`, an exercise module in
  `src/de_berg_geometry/exercises/`, and focused tests in `tests/`.
- Do not make a lesson depend on the learner having completed a later lesson.
- Prefer small geometric examples whose expected result can be checked by hand.
- Exercise modules may contain `NotImplementedError`; the corresponding lesson tests are expected
  to fail until the learner completes the task.
- Keep the infrastructure test passing even while exercise tests are incomplete.
