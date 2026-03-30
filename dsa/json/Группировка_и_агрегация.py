"""
Дан список JSON-объектов (как из базы данных).
Сгруппируй по полю, посчитай агрегаты — среднее, сумму, количество.

users = [
    {"name": "Alice", "dept": "eng", "salary": 120000},
    {"name": "Bob",   "dept": "eng", "salary": 95000},
    {"name": "Carol", "dept": "hr",  "salary": 80000},
]

→ {
    "eng": {"count": 2, "avg_salary": 107500, "total": 215000},
    "hr":  {"count": 1, "avg_salary": 80000,  "total": 80000}
}

Размышления
    сгруппировать по полю dept
        посчитать кол-во вхождений (cnt)
        посчитать среднее (salary / cnt)
"""


def aggregate(users: list[dict]) -> dict:
    agg = {}

    for user in users:
        dept = user["dept"]
        salary = user["salary"]

        if dept not in agg:
            agg[dept] = {"count": 0, "total": 0}

        agg[dept]["count"] += 1
        agg[dept]["total"] += salary

    # считаем среднее отдельно
    for dept in agg:
        total = agg[dept]["total"]
        count = agg[dept]["count"]
        agg[dept]["avg_salary"] = total / count
    return agg


from collections import defaultdict


def aggregate_v2(users: list[dict]) -> dict:
    agg = defaultdict(lambda: {"count": 0, "total": 0, "avg_salary": 0})
    for u in users:
        d = agg[u["dept"]]
        d["count"] += 1
        d["total"] += u["salary"]
        d["avg_salary"] = d["total"] / d["count"]

    return agg


if __name__ == "__main__":

    def test_aggregate_basic():
        users = [
            {"name": "Alice", "dept": "eng", "salary": 120000},
            {"name": "Bob", "dept": "eng", "salary": 95000},
            {"name": "Carol", "dept": "hr", "salary": 80000},
        ]

        result = aggregate_v2(users)

        expected = {
            "eng": {"count": 2, "total": 215000, "avg_salary": 107500.0},
            "hr": {"count": 1, "total": 80000, "avg_salary": 80000.0},
        }

        print(result)
        assert result == expected

    test_aggregate_basic()
