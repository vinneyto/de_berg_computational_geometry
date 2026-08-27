# Computational Geometry: from segments to map overlay

Практический курс по второй главе книги de Berg et al. *Computational Geometry*.
Он превращает плотное изложение книги в маленькие Python-упражнения с тестами.

К концу курса вы самостоятельно соберёте цепочку:

```text
геометрические предикаты
→ пересечение двух отрезков
→ очередь событий и sweep status
→ Bentley–Ottmann
→ DCEL
→ разрезание рёбер
→ границы и отверстия
→ overlay и Boolean operations
```

## Быстрый старт

```bash
uv sync
uv run pytest tests/test_course_structure.py
uv run pytest tasks/task_01_predicates/test_exercise.py
```

Первый инфраструктурный тест должен проходить сразу. Тест упражнения должен сначала упасть с
`NotImplementedError` — это точка старта, а не поломка репозитория.

Рабочий цикл для каждого урока:

1. Откройте `README.md` нужного задания в `tasks/`.
2. Рядом откройте `exercise.py` и `test_exercise.py`. Если застряли, используйте `HINT.md`.
3. Запустите только тест этого урока.
4. Реализуйте отмеченные функции, пока тест не станет зелёным.
5. Запустите все уже пройденные тесты, например первые четыре:
   `uv run pytest tasks/task_{01..04}_*/test_exercise.py`.

Полная карта курса находится в [COURSE.md](COURSE.md).

## Почему структуры иногда готовые

Цель курса — понять обязанности структуры, а не повторно писать стандартную библиотеку.
Поэтому очередь событий строится поверх `heapq`, упорядоченное множество — поверх
`sortedcontainers`, а Shapely используется в конце как проверочный оракул. DCEL реализуется
самостоятельно, потому что именно её связи составляют центральную идею второй половины главы.

## Проверки качества

```bash
uv run pytest tests/test_course_structure.py
uv run ruff check .
```

Полный `uv run pytest` станет зелёным после прохождения всех заданий.

## Сокращения

- **DCEL** — *doubly-connected edge list*, двусвязный список рёбер.
- **CCW** — *counterclockwise*, направление против часовой стрелки.
- **CW** — *clockwise*, направление по часовой стрелке.
- **BST** — *binary search tree*, двоичное дерево поиска.
- **AABB** — *axis-aligned bounding box*, ограничивающий прямоугольник по осям.
- **U(p), L(p), C(p)** — upper endpoints, lower endpoints и containing segments:
  верхние концы, нижние концы и сегменты, содержащие точку во внутренности.
- **XOR** — *exclusive OR*, исключающее «или».
