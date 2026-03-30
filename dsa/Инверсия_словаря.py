"""
Инверсия словаря
Инвертируй словарь: ключи становятся значениями, значения — ключами. Если несколько ключей имеют одно значение — собери их в список.
{"a":1,"b":2,"c":1} → {1:["a","c"], 2:["b"]}
Что если значения сами являются списками? Это бонусный вопрос.

{
    "a":1,
    "b":2,
    "c":1
}

{1:["a","c"], 2:["b"]}

Размышления
    нам нужен словарь ключ -> список
    Что если значения сами являются списками? Это бонусный вопрос.
    список не может являться ключом в словаре, так как это изменяемый тип данных, словарь в качестве ключа поддерживает только неизменямые типы
"""

from collections import defaultdict


def invert(input: dict[str, int]) -> dict[int, list[str]]:
    res: dict[int, list[str]] = defaultdict(list)
    for k, v in input.items():
        res[v].append(k)
    return res


def invert_v2(
    data: dict[str, int | list[int]],
) -> dict[tuple[int, ...] | int, list[str]]:
    res: dict[tuple[int, ...] | int, list[str]] = defaultdict(list)
    for k, v in data.items():
        key = tuple(v) if isinstance(v, list) else v
        res[key].append(k)
    return res


if __name__ == "__main__":
    print(invert_v2({"a": 1, "b": 2, "c": 1}))  # {1: ['a', 'c'], 2: ['b']}
    print(
        invert_v2({"a": [1, 2], "b": [1, 2], "c": 1})
    )  # {(1,2): ['a', 'b'], 1: ['c']}
