"""
Дан лог оценок студентов по предметам.
Построй таблицу
    где строки — студенты,
    колонки — предметы,
    значения — средняя оценка.

Если студент не сдавал предмет — поставь None.
Добавь колонку avg — средняя по всем предметам студента (только где не None).

grades = [
    {"student": "Alice", "subject": "math",    "score": 90},
    {"student": "Alice", "subject": "math",    "score": 80},  # два экзамена
    {"student": "Alice", "subject": "english", "score": 70},
    {"student": "Bob",   "subject": "math",    "score": 60},
    {"student": "Bob",   "subject": "physics", "score": 75},
    {"student": "Carol", "subject": "english", "score": 95},
]

# ожидается:
[
    {"student": "Alice", "math": 85.0, "english": 70.0, "physics": None, "avg": 77.5},
    {"student": "Bob",   "math": 60.0, "english": None, "physics": 75.0, "avg": 67.5},
    {"student": "Carol", "math": None, "english": 95.0, "physics": None, "avg": 95.0},
]

Idea
    [1] traverse and group by student name and put subject, attempts, score (score / attempts)
    {
        "Alice": {"math": {"attempts": 2, "score": 85.0}, "english": {"attempts": 1, "score": 70.0}},
        ...
    }
    + we kepts all seen subjects (set) [math, english, ...]
    [2] traverse groups and per group for group we all subjects
"""

from collections import defaultdict


def pivot_grades(grades: list[dict]) -> list[dict]:
    subjects = set()
    # student -> subject -> stats
    students = defaultdict(lambda: defaultdict(lambda: {"attempts": 0, "score": 0}))

    # [1] группировка
    for g in grades:
        st, su, sc = g["student"], g["subject"], g["score"]

        entry = students[st][su]
        entry["attempts"] += 1
        entry["score"] += sc

        subjects.add(su)

    # [2] считаем средние по предметам
    for st in students:
        for su in students[st]:
            entry = students[st][su]
            entry["score"] /= entry["attempts"]

    # [3] собираем pivot + avg
    result = []
    for st, exams in students.items():
        row = {"student": st}

        total = 0
        count = 0

        for su in subjects:
            if su in exams:
                score = exams[su]["score"]
                row[su] = score

                total += score
                count += 1
            else:
                row[su] = None

        row["avg"] = total / count if count else None

        result.append(row)

    return result
