"""
JOIN — это объединение двух таблиц по общему ключу.
Наивный способ — вложенный цикл O(n·m).
Правильный — сначала построить lookup dict из одной таблицы, потом проходить по второй за O(n).


Left join с агрегацией (простая)

Даны два списка: пользователи и их заказы.
Верни список всех пользователей с количеством заказов и суммарной выручкой.
Если у пользователя нет заказов — верни 0 для обоих полей.

users = [
    {"user_id": 1, "name": "Alice"},
    {"user_id": 2, "name": "Bob"},
    {"user_id": 3, "name": "Carol"},  # у Carol нет заказов
]

orders = [
    {"order_id": 1, "user_id": 1, "amount": 500},
    {"order_id": 2, "user_id": 1, "amount": 300},
    {"order_id": 3, "user_id": 2, "amount": 800},
]

# ожидается:
[
    {"user_id": 1, "name": "Alice", "order_count": 2, "total": 800},
    {"user_id": 2, "name": "Bob",   "order_count": 1, "total": 800},
    {"user_id": 3, "name": "Carol", "order_count": 0, "total": 0},
]

Idea
    traversre orders group by users by
"""

from collections import defaultdict


def aggregate_orders(orders: list[dict]) -> dict[int, dict]:
    agg = defaultdict(lambda: {"order_count": 0, "total": 0})

    for o in orders:
        user_id = o["user_id"]
        agg[user_id]["order_count"] += 1
        agg[user_id]["total"] += o["amount"]

    return agg


def left_join_users(users: list[dict], orders: list[dict]) -> list[dict]:
    agg = aggregate_orders(orders)

    result = []
    for u in users:
        user_id = u["user_id"]
        stats = agg[user_id]  # defaultdict даст 0, если нет заказов

        result.append(
            {
                "user_id": user_id,
                "name": u["name"],
                "order_count": stats["order_count"],
                "total": stats["total"],
            }
        )

    return result
