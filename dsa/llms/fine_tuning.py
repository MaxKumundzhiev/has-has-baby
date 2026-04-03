"""
Fine-tuning это дообучение предобученной модели на своих данных.
Модель уже умеет понимать язык — ты учишь её конкретной задаче или стилю.

Дан сырой лог пользовательских запросов в службу поддержки.
Подготовь датасет для fine-tuning модели которая классифицирует тип запроса и генерирует ответ.

Idea
    iterate over raw logs, for each log
        category = classify(text) -> return 1 of 4 classes
        normalized = normalize(text) -> return normalized text
        example = build_training_example(normalized)
        add example to the dataset
    split dataset (stratified approach) -> returns train, eval, test samples
"""

raw_logs = [
    "my order #1234 hasn't arrived yet it's been 2 weeks",
    "I WANT REFUND FOR ORDER 5678 IT WAS BROKEN!!!",
    "how do i change my password?",
    "the app keeps crashing on iphone 14",
    "where is my package? order number 9999",
    "can't login to my account since yesterday",
    "i want to return item from order #3333",
    "app crashes every time i open it",
    "reset password not working",
    "order 7777 still not delivered after 3 weeks",
]

CATEGORIES = {
    "delivery": ["order", "arrived", "package", "delivered", "weeks"],
    "refund": ["refund", "return", "broken"],
    "technical": ["crash", "crashing", "login", "password", "app"],
}

RESPONSES = {
    "delivery": "We apologize for the delay. Please share your order number and we'll investigate immediately.",
    "technical": "Sorry for the inconvenience. Please try reinstalling the app or clearing cache. If issue persists, contact support.",
    "refund": "We're sorry to hear that. Please initiate a return request in your account and we'll process it within 3-5 days.",
    "unknown": "Thank you for contacting us. Could you please provide more details about your issue?",
}

from collections import defaultdict


def classify(text: str, categories: dict) -> str:
    """
    Определи категорию по ключевым словам.
    Если слова из нескольких категорий — выбери с наибольшим совпадением.
    Если совпадений нет — верни "unknown".
    """
    words = set(text.lower().split())  # lower — иначе "ORDER" ≠ "order"
    scores = {}
    for category, keywords in categories.items():
        matches = words & set(keywords)
        scores[category] = len(matches) / len(words) if words else 0

    if all(v == 0 for v in scores.values()):
        return "unknown"

    return max(scores, key=lambda c: scores[c])


def normalize(text: str) -> str:
    """
    Нормализуй текст: lower, убери лишние пробелы.
    Не убирай пунктуацию — она важна для обучения.
    Шаги:
        1. strip() — убираем пробелы по краям
        2. lower() — приводим к нижнему регистру
        3. split() + join() — схлопываем несколько пробелов в один
           "hello   world" → ["hello", "world"] → "hello world"
    """
    if not text.strip():
        return ""
    return " ".join(text.strip().lower().split())


def build_training_example(text: str, category: str, answer: str) -> dict:
    """
    Из сырого текста собери пример для fine-tuning:
    {
        "messages": [
            {"role": "system",    "content": "You are a customer support classifier..."},
            {"role": "user",      "content": <нормализованный текст>},
            {"role": "assistant", "content": <категория: ответ>},
        ]
    }
    """
    return {
        "messages": [
            {"role": "system", "content": "You are a customer support classifier..."},
            {"role": "user", "content": text},
            {"role": "assistant", "content": f"{category}:{answer}"},
        ]
    }


def prepare_dataset(logs: list[str]) -> dict:
    """
    Собери датасет из всех логов.
    Раздели на train (80%) и val (20%) — стратифицированно по категории.
    Верни {"train": [...], "val": [...], "stats": {категория: count}}
    """
    dataset: list[dict] = []
    for log in logs:
        category: str = classify(log, CATEGORIES)
        normalized: str = normalize(log)
        example: dict = build_training_example(
            normalized, category, RESPONSES[category]
        )
        dataset.append(example)


dataset = prepare_dataset(raw_logs)
print(f"Train: {len(dataset['train'])}")
print(f"Val:   {len(dataset['val'])}")
print(f"Stats: {dataset['stats']}")
print("\nПример:")
print(dataset["train"][0])
