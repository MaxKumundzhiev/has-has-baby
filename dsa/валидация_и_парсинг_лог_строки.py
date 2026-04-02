"""
Дан список строк из access-лога.
Распарси каждую строку и верни список валидных записей.
Невалидные — собери отдельно с причиной ошибки.

Формат строки:
```
"2024-01-15 ERROR user@example.com Failed login attempt"
 ^дата       ^level ^email           ^message


logs = [
    "2024-01-15 ERROR user@example.com Failed login attempt",
    "2024-01-16 INFO  admin@site.org   Server started",
    "not-a-date INFO  user@example.com Something",    # невалидная дата
    "2024-01-17 DEBUG bad-email        Message here", # невалидный email
    "2024-01-18 CRITICAL",                            # не хватает полей
]

# ожидается:
{
    "valid": [
        {"date": "2024-01-15", "level": "ERROR", "email": "user@example.com", "message": "Failed login attempt"},
        {"date": "2024-01-16", "level": "INFO", "email": "admin@site.org",   "message": "Server started"},
    ],
    "invalid": [
        {"raw": "not-a-date INFO ...", "reason": "invalid date format"},
        {"raw": "2024-01-17 DEBUG ...", "reason": "invalid email"},
        {"raw": "2024-01-18 CRITICAL", "reason": "missing fields"},
    ]
}
"""

import re
from collections import defaultdict


VALID_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


def valid_date(val: str) -> tuple[bool, str]:
    if re.match(r"^\d{4}-\d{2}-\d{2}$", val):
        return True, ""
    return False, "invalid date format"


def valid_level(val: str) -> tuple[bool, str]:
    if val in VALID_LEVELS:
        return True, ""
    return False, f"invalid level: {val}"


def valid_email(val: str) -> tuple[bool, str]:
    if re.match(r"^[\w.+-]+@[\w-]+\.[a-z]{2,}$", val):
        return True, ""
    return False, "invalid email"


def parse_logs(logs: list[str]) -> dict:
    res = {"valid": [], "invalid": []}

    for log in logs:
        parts = log.split(maxsplit=3)

        if len(parts) < 4:
            res["invalid"].append({"raw": log, "reason": "missing fields"})
            continue

        date, level, email, message = parts
        for value, validator in [
            (date, valid_date),
            (level, valid_level),
            (email, valid_email),
        ]:
            ok, reason = validator(value)
            if not ok:
                res["invalid"].append({"raw": log, "reason": reason})
                break
        else:
            res["valid"].append(
                {"date": date, "level": level, "email": email, "message": message}
            )
    return res


if __name__ == "__main__":
    logs = [
        "2024-01-15 ERROR user@example.com Failed login attempt",
        "2024-01-16 INFO  admin@site.org   Server started",
        "not-a-date INFO  user@example.com Something",  # невалидная дата
        "2024-01-17 DEBUG bad-email        Message here",  # невалидный email
        "2024-01-18 CRITICAL",  # не хватает полей
    ]
    print(parse_logs(logs))
