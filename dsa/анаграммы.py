"""
Анаграммы
Дан список слов. Сгруппируй их так, чтобы анаграммы оказались вместе. Верни список групп.
["eat","tea","tan","ate","nat","bat"]
→ [["eat","tea","ate"],["tan","nat"],["bat"]]
Как превратить слово в ключ, одинаковый для всех его анаграмм?

Размышления
    анаграмма - перестановка бука дает нам одно и то же слово
    использовать словарь где ключом будем отсортированное слово по возврастанию
"""


def anagramma(arr: list[str]) -> list[list[str]]:
    if not arr:
        return []

    groups: dict[str, list[str]] = {}
    for w in arr:
        key: str = "".join(sorted(w))
        if key not in groups:
            groups[key] = []
        groups[key].append(w)
    return [v for (k, v) in groups.items()]


from collections import defaultdict


def anagramma_v2(arr: list[str]) -> list[list[str]]:
    if not arr:
        return []

    groups: dict[str, list[str]] = defaultdict(list)
    for w in arr:
        key: str = "".join(sorted(w))
        groups[key].append(w)
    return [v for (k, v) in groups.items()]


if __name__ == "__main__":
    arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    print(anagramma(arr))
    assert anagramma(arr) == res
