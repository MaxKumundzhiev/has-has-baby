"""
Три таблицы: продавцы, продажи, продукты.

Построй pivot-отчёт:
    строки — продавцы,
    колонки — категории продуктов,
    значения — суммарная выручка.

Добавь колонку total и строку "TOTAL" в конце с суммами по каждой колонке.


sellers = [
    {"seller_id": 1, "name": "Ivan"},
    {"seller_id": 2, "name": "Maria"},
]

sales = [
    {"seller_id": 1, "product_id": 1, "revenue": 1200},
    {"seller_id": 1, "product_id": 1, "revenue": 800},
    {"seller_id": 1, "product_id": 3, "revenue": 150},
    {"seller_id": 2, "product_id": 2, "revenue": 600},
    {"seller_id": 2, "product_id": 3, "revenue": 200},
]

products = [
    {"product_id": 1, "name": "laptop",  "category": "electronics"},
    {"product_id": 2, "name": "phone",   "category": "electronics"},
    {"product_id": 3, "name": "t-shirt", "category": "clothing"},
]

# ожидается:
[
    {"seller": "Ivan",  "electronics": 2000, "clothing": 150,  "total": 2150},
    {"seller": "Maria", "electronics": 600,  "clothing": 200,  "total": 800},
    {"seller": "TOTAL", "electronics": 2600, "clothing": 350,  "total": 2950},
]

Flow
    lookup sellers
    {
        1: {"name": ...}
    }
"""

from collections import defaultdict


def sales_pivot(sellers, products, sales) -> list[dict]:
    # шаг 1 — lookup таблицы
    seller_by_id = {s["seller_id"]: s["name"] for s in sellers}
    category_by_id = {p["product_id"]: p["category"] for p in products}
    categories = sorted(set(category_by_id.values()))

    # шаг 2 — группируем выручку: seller_id → category → сумма
    groups = defaultdict(lambda: defaultdict(float))
    col_totals = defaultdict(float)

    for sale in sales:
        s_id = sale["seller_id"]
        cat = category_by_id.get(sale["product_id"])
        if cat is None:
            continue
        groups[s_id][cat] += sale["revenue"]

    # шаг 3 — собираем pivot строки
    result = []
    for s_id, cat_revenue in groups.items():
        row = {"seller": seller_by_id[s_id]}
        row_total = 0

        for cat in categories:
            val = cat_revenue.get(cat, 0)
            row[cat] = val
            row_total += val
            col_totals[cat] += val

        row["total"] = row_total
        result.append(row)

    # шаг 4 — строка TOTAL
    total_row = {"seller": "TOTAL"}
    grand_total = 0
    for cat in categories:
        total_row[cat] = col_totals[cat]
        grand_total += col_totals[cat]
    total_row["total"] = grand_total
    result.append(total_row)

    return result


sellers = [
    {"seller_id": 1, "name": "Ivan"},
    {"seller_id": 2, "name": "Maria"},
]
products = [
    {"product_id": 1, "name": "laptop", "category": "electronics"},
    {"product_id": 2, "name": "phone", "category": "electronics"},
    {"product_id": 3, "name": "t-shirt", "category": "clothing"},
]
sales = [
    {"seller_id": 1, "product_id": 1, "revenue": 1200},
    {"seller_id": 1, "product_id": 1, "revenue": 800},
    {"seller_id": 1, "product_id": 3, "revenue": 150},
    {"seller_id": 2, "product_id": 2, "revenue": 600},
    {"seller_id": 2, "product_id": 3, "revenue": 200},
]

for row in sales_pivot(sellers, products, sales):
    print(row)
