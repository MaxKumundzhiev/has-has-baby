"""
GROUP BY, JOIN, pivot
Разберём все три операции на одном сквозном примере — данные о заказах и пользователях.

# исходные данные — будем использовать во всех примерах
users = [
    {"user_id": 1, "name": "Alice", "city": "Moscow"},
    {"user_id": 2, "name": "Bob",   "city": "Berlin"},
    {"user_id": 3, "name": "Carol", "city": "Moscow"},
]

orders = [
    {"order_id": 1, "user_id": 1, "category": "electronics", "amount": 1200},
    {"order_id": 2, "user_id": 1, "category": "books",       "amount": 300},
    {"order_id": 3, "user_id": 2, "category": "electronics", "amount": 800},
    {"order_id": 4, "user_id": 3, "category": "books",       "amount": 150},
    {"order_id": 5, "user_id": 3, "category": "electronics", "amount": 950},
    {"order_id": 6, "user_id": 2, "category": "books",       "amount": 200},
]

GROUP BY
    Идея: собрать записи в корзины по ключу, потом агрегировать каждую корзину.
    Размышления:
        реализуем ф group_by(records: list[dict], key: str) - то есть группирует по любому ключу
"""

from collections import defaultdict
from dataclasses import dataclass


def group_by(records: list[dict], key: str) -> dict[str, list]:
    """
    key=user_id
    records=orders
    {
        1: [
            {"order_id": 1, "user_id": 1, "category": "electronics", "amount": 1200},
            {"order_id": 2, "user_id": 1, "category": "books",       "amount": 300},
        ],
        3: [
            {"order_id": 4, "user_id": 3, "category": "books",       "amount": 150},
            {"order_id": 5, "user_id": 3, "category": "electronics", "amount": 950},
        ],
        ...
    }
    """
    groups: dict[str, list] = defaultdict(list)
    for r in records:
        groups[r[key]].append(r)
    return dict(groups)


def aggregate(records: list[dict], group_key: str, value_key: str) -> list[dict]:
    # 1 first group by provided key
    groups = defaultdict(list)
    for r in records:
        groups[r[group_key]].append(r[value_key])

    # 2 aggregate (count, sum, avg, min, max)
    result = []
    for group, values in groups.items():
        result.append(
            {
                group_key: group,
                "count": len(values),
                "sum": sum(values),
                "avg": round(sum(values) / len(values), 2),
                "min": min(values),
                "max": max(values),
            }
        )
    return sorted(result, key=lambda x: x["sum"], reverse=True)


users = [
    {"user_id": 1, "name": "Alice", "city": "Moscow"},
    {"user_id": 2, "name": "Bob", "city": "Berlin"},
    {"user_id": 3, "name": "Carol", "city": "Moscow"},
]

orders = [
    {"order_id": 1, "user_id": 1, "category": "electronics", "amount": 1200},
    {"order_id": 2, "user_id": 1, "category": "books", "amount": 300},
    {"order_id": 3, "user_id": 2, "category": "electronics", "amount": 800},
    {"order_id": 4, "user_id": 3, "category": "books", "amount": 150},
    {"order_id": 5, "user_id": 3, "category": "electronics", "amount": 950},
    {"order_id": 6, "user_id": 2, "category": "books", "amount": 200},
]

by_user = aggregate(orders, group_key="user_id", value_key="amount")
print(by_user)
by_category = aggregate(orders, group_key="category", value_key="amount")
print(by_category)
