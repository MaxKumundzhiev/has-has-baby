"""
Даны два JSON-объекта. Найди разницу между ними — какие ключи добавились, удалились, или изменили значение.

a = {"name": "Alice", "age": 30, "city": "Moscow"}
b = {"name": "Alice", "age": 31, "country": "Russia"}

{
    "changed": {"age": (30, 31)},
    "added":   {"country": "Russia"},
    "removed": {"city": "Moscow"}
}

Размышления
    разобьем задачу на три
        - найти ключи которые добавились (те есть во втором множестве, но нет в первом) b.difference(a)
        - найти ключи которые изменились (те есть те ключи которые есть и в 1 и во 2 множствах И их не равны) a.intersection(b) -> trraverse
        - найти ключи которые удалились  (те есть в первом множестве, но нет во втором) a.difference(b)
"""

from typing import Any


def jsons_difference(
    d1: dict[str, Any], d2: dict[str, Any]
) -> dict[str, dict[str, Any]]:
    s1 = set(d1)
    s2 = set(d2)

    # добавленные ключи
    added = {}
    for key in s2 - s1:
        added[key] = d2[key]

    # удалённые ключи
    removed = {}
    for key in s1 - s2:
        removed[key] = d1[key]

    # изменённые значения
    changed = {}
    for key in s1 & s2:
        if d1[key] != d2[key]:
            changed[key] = (d1[key], d2[key])

    return {
        "changed": changed,
        "added": added,
        "removed": removed,
    }


if __name__ == "__main__":
    a = {"name": "Alice", "age": 30, "city": "Moscow"}
    b = {"name": "Alice", "age": 31, "country": "Russia"}
    res = jsons_difference(a, b)
    print(res)
