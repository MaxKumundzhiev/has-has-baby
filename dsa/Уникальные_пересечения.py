"""
Уникальные пересечения
Дан список из N списков. Найди элементы, которые встречаются хотя бы в двух из них, но не во всех сразу.
[[1,2,3],[2,3,4],[4,5]] → {2,3,4}
Подсказка: подумай о разнице между union, intersection и symmetric_difference.


Размышления
    посчитать сколько раз каждый (уникального) эелмент входит в входящие списки
"""


def unique_intersection(arrays: list[list[int]]) -> set[int]:
    freq: dict[int, int] = {}
    for arr in arrays:
        arr = set(arr)  # remove duplicates
        for v in arr:
            freq[v] = freq.get(v, 0) + 1

    """
    словарь частотности значений в кажлм списке
    [[1,2,3],[2,3,4],[4,5]]
    # value: frequency
    {
        1: 1
        2: 2
        3: 2
        4: 2
        5: 1
    }
    """

    res: set[int] = set()
    for v, cnt in freq.items():
        if 1 < cnt < len(arrays):
            res.add(v)
    return res


from collections import Counter


def unique_intersection_v2(arrays: list[list[int]]) -> set[int]:
    n = len(arrays)
    counts = Counter(el for lst in arrays for el in set(lst))
    return {el for el, cnt in counts.items() if 1 < cnt < n}
