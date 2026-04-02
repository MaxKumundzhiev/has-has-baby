"""
Дан текст.
Верни N самых частых слов в виде list[tuple[str, int]],
отсортированных по убыванию частоты.

Знаки препинания игнорировать, регистр не важен.

text = "the cat sat on the mat the cat sat"
top_words(text, n=3)
# → [("the", 3), ("cat", 2), ("sat", 2)]
# при равной частоте — алфавитный порядок
"""

import re
from collections import defaultdict


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    if not text.strip():
        return []

    words = re.sub(r"[^\w\s]", "", text.lower()).split()

    freq: dict[str, int] = defaultdict(int)
    for w in words:
        freq[w] += 1

    sorted_words = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:n]
