"""
Дан список объектов и шаблон преобразования (маппинг старых ключей в новые,
с поддержкой вложенности и значений по умолчанию).

data = {"first_name": "Alice", "last_name": "Smith", "age": 30}

template = {
    "name":    "first_name",
    "surname": "last_name",
    "info": {
        "years": "age",
        "city":  ("city", "Unknown")  # (ключ, дефолт)
    }
}

→ {
    "name": "Alice",
    "surname": "Smith",
    "info": {
        "years": 30,
        "city": "Unknown"
    }
}

Размышления
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Info:
    name: Optional[str] = None
    city: str = field(default="Unknown")


@dataclass
class Template:
    name: Optional[str] = None
    surname: Optional[str] = None
    info: Info = field(default_factory=Info)  # создаёт Info автоматически


def map_data(data: dict) -> Template:
    # создаём объект, подставляя значения из словаря
    return Template(
        name=data.get("name"),
        surname=data.get("surname"),
        info=Info(name=data.get("info_name"), city=data.get("info_city", "Unknown")),
    )
