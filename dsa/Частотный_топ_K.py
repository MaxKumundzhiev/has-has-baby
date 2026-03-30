"""
Частотный топ-K
Дана строка текста. Найди K самых частых слов и верни их в виде словаря {слово: количество}, отсортированного по убыванию.
("the cat sat on the mat", k=3) → {"the":2,"cat":1,"sat":1}
Без Counter из collections — только чистые dict-операции.

Размышления
    преобразуем входные данные в список слов разделенных по пробелу
    заведет словарь частотностей
    проитерируемся по массиву слово и посчитаем кол-во частот каждого

    ... (сортировать словарь по значению)
    {
        the: 2
        cat: 1
        sat: 1
        on: 1
        mat: 1
    }
    key-val --> val-key
    преаллоцируем список списков
    где индексом будет являться частотность
    [
        [],
        [cat, sat, on, mat],
        [the],
        [],
        [],
        [],
    ]
"""

from collections import defaultdict


def k_most_words(data: str, k: int) -> dict[str, int]:
    words: list[str] = data.split()
    counter: dict[str, int] = defaultdict(int)

    for w in words:
        counter[w] += 1

    top: list[list[str]] = [[] for _ in range(len(words) + 1)]
    for word, freq in counter.items():  # ✅ не перезаписываем k
        top[freq].append(word)

    top_k: dict[str, int] = {}
    remaining = k
    for i, bucket in enumerate(reversed(top)):
        if remaining == 0:
            break
        if not bucket:
            continue
        real_freq = len(top) - 1 - i  # ✅ реальная частотность
        for word in bucket:
            if remaining == 0:
                break
            top_k[word] = real_freq
            remaining -= 1

    return top_k


def k_most_words_v2(data: str, k: int) -> dict[str, int]:
    counter: dict[str, int] = {}
    for w in data.split():
        counter[w] = counter.get(w, 0) + 1
    sorted_pairs = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_pairs[:k])


def k_most_words_v3(data: str, k: int) -> dict[str, int]:
    import heapq

    counter: dict[str, int] = {}
    for w in data.split():
        counter[w] = counter.get(w, 0) + 1
    top_k = heapq.nlargest(k, counter.items(), key=lambda x: x[1])
    return dict(top_k)


if __name__ == "__main__":
    print(k_most_words("the cat sat on the mat", k=3))
    # {"the": 2, "cat": 1, "sat": 1}
