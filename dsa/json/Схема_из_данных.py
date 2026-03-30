"""
Дан список JSON-объектов с разными полями.
Выведи схему — какие поля встречаются, их типы, и в какой доле объектов они присутствуют.

data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob",   "age": None, "city": "Moscow"},
    {"name": "Carol"},
]

→ {
    "name": {"type": "str",  "coverage": 1.0},
    "age":  {"type": "int",  "coverage": 0.67},
    "city": {"type": "str",  "coverage": 0.33}
}

Размышления
    хэшмапа для полей
    доля объектов они присутствуют
        общее кол-во рекордов / частотность ключа

    if v in scheme:
        {
            "name": {"type": "str", "coverage": 0}
            "age": {"type": "int", "coverage": 0}
        }

    {
        "name": 1
        "age": 1
    }
"""

from collections import defaultdict


def scheme_check(data: list[dict]) -> dict:
    scheme = defaultdict(lambda: {"type": "", "coverage": 0.0})
    counter = defaultdict(int)

    for r in data:
        for i in r.items():
            k, v = i
            if k not in scheme:
                s = scheme[k]
                s["type"] = type(v).__name__
            counter[k] += 1

    total_recs: int = len(data)
    for k, i in scheme.items():
        scheme[k]["coverage"] = round(counter[k] / total_recs, 2)

    return scheme


if __name__ == "__main__":
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": None, "city": "Moscow"},
        {"name": "Carol"},
    ]
    res = dict(scheme_check(data))
    print(res)
