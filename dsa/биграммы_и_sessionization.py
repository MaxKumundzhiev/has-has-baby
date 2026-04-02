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

2 part
Часть B — раздели сообщения на сессии:
    если между двумя соседними сообщениями больше 30 минут — это новая сессия.
    Для каждой сессии верни номер, количество сообщений и топ-1 биграмму.


"""

from collections import defaultdict
from datetime import datetime


def bigrams(text: str) -> list[str]:
    return [f"{w1} {w2}" for w1, w2 in zip(text, text[1:])]


def top_bigrams(messages: list[dict], n: int) -> list[tuple[str, int]]:
    freq: dict[str, int] = defaultdict(int)
    for msg in messages:
        text = msg["text"]
        bigrams_: list[str] = bigrams(text)
        for bg in bigrams_:
            freq[bg] += 1
    return list[freq.items()]


def pipeline(messages, n: int = 3):
    fmt = "%Y-%m-%d %H:%M"
    # part A (top n bigrams across all the messages)
    top: list[tuple[str, int]] = top_bigrams(messages, n)

    # part B ()
    sessions = []
    current: list[dict] = [messages[0]]
    prev_ts = datetime.strftime(messages[0]["ts"], fmt)

    for msg in messages[1:]:
        ts = datetime.strftime(msg["ts"], fmt)
        diff = (ts - prev_ts).total_seconds() / 60

        if diff > 30:  # новая сессия
            sessions.append(current)
            current = []

        current.append(msg)
        prev_ts = ts

    sessions.append(current)  # последняя сессия

    result = []
    for i, session in enumerate(sessions):
        freq: dict[str, int] = defaultdict(int)
        for msg in session:
            for bg in bigrams(msg["text"]):
                freq[bg] += 1
        top_bg = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        result.append(
            {
                "session": i + 1,
                "messages": len(session),
                "top_bigram": top_bg[0][0] if top_bg else None,
            }
        )

    return {"top_bigrams": top[:n], "sessions": result}


if __name__ == "__main__":
    messages = [
        {"ts": "2024-01-15 10:00", "text": "hello world how are you"},
        {"ts": "2024-01-15 10:05", "text": "hello world again today"},
        {"ts": "2024-01-15 10:08", "text": "how are you doing today"},
        {"ts": "2024-01-15 11:00", "text": "new session hello world"},
        {"ts": "2024-01-15 11:10", "text": "hello world one more time"},
    ]
    pipeline(messages)
