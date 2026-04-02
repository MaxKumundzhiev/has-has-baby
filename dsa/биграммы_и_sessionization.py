"""
Часть A — биграммы
Напиши функцию bigrams(text) которая возвращает все пары соседних слов из текста.
Потом top_bigrams(messages, n) — топ-N биграмм по всем сообщениям вместе.

messages = [
    {"ts": "2024-01-15 10:00", "text": "hello world how are you"},
    {"ts": "2024-01-15 10:05", "text": "hello world again today"},
    {"ts": "2024-01-15 10:08", "text": "how are you doing today"},
    {"ts": "2024-01-15 11:00", "text": "new session hello world"},
    {"ts": "2024-01-15 11:10", "text": "hello world one more time"},
]

top_bigrams(messages, n=3)
# → [("hello world", 4), ("how are", 2), ("are you", 2)]
# при равной частоте — алфавитный порядок


Idea
    traverse msg (msg.get("text"))
    call bigrams -> [word and its neighbour]
    add to frequency dict by key
"""

from collections import defaultdict


def bigrams(text: str) -> list[str]:
    words = text.split()
    return [f"{w1} {w2}" for w1, w2 in zip(words, words[1:])]


def top_bigrams(messages: list[dict], n: int) -> list[tuple[str, int]]:
    freq: dict[str, int] = defaultdict(int)
    for msg in messages:
        bigrams_: list[str] = bigrams(msg["text"])
        for bg in bigrams_:
            freq[bg] += 1

    sorted_items = sorted(freq.items(), key=lambda i: (-i[1], i[0]))
    return sorted_items[:n]


messages = [
    {"ts": "2024-01-15 10:00", "text": "hello world how are you"},
    {"ts": "2024-01-15 10:05", "text": "hello world again today"},
    {"ts": "2024-01-15 10:08", "text": "how are you doing today"},
    {"ts": "2024-01-15 11:00", "text": "new session hello world"},
    {"ts": "2024-01-15 11:10", "text": "hello world one more time"},
]
print(top_bigrams(messages, 3))
