"""
Дан глубоко вложенный JSON-объект. Преобразуй его в плоский словарь,
где ключи — это путь через вложенность через точку.

{
    "user": {
        "name": "Alice",
        "address": {
            "city": "Moscow",
            "zip": "101000"
        }
    }
}
→ {"user.name": "Alice", "user.address.city": "Moscow", "user.address.zip": "101000"}

Подсказка: думай рекурсивно.
Размышления
    что если рекурсивно на ключ вызывать погружение
    воспользоваться обходом в глубину (рекурсивным)

def traverse(entry: dict[Any]):
    if not entry.keys():
        return entry.values()

    traverse(entry.keys())
"""

from typing import Any

"""
{
    "user": {
        "name": "Alice",
        "address": {
            "city": "Moscow",
            "zip": "101000"
        }
    }
}

result = {

}
"""


def flatten_json_to_dict(data: dict[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}

    def flatten(value: dict | list | str, parent_key: str = "", separator: str = "."):
        if isinstance(value, dict):
            for key, sub_value in value.items():
                new_key = f"{parent_key}{separator}{key}" if parent_key else key
                flatten(sub_value, new_key)
        elif isinstance(value, list):
            for index, sub_value in enumerate(value):
                new_key = (
                    f"{parent_key}{separator}{index}" if parent_key else str(index)
                )
                flatten(sub_value, new_key)
        else:
            result[parent_key] = value

    flatten(data)
    return result


def flatten_dict_to_json_v2(data: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}

    def flatten(
        entry: dict | list | Any,
        parent_key: str = "",
        separator: str = ".",
    ) -> None:
        # если словарь — идём вглубь
        if isinstance(entry, dict):
            for k, sub_entry in entry.items():
                key = f"{parent_key}{separator}{k}" if parent_key else k
                flatten(entry=sub_entry, parent_key=key, separator=separator)

        # если список — тоже идём вглубь
        elif isinstance(entry, list):
            for i, sub_entry in enumerate(entry):
                key = f"{parent_key}{separator}{i}" if parent_key else str(i)
                flatten(entry=sub_entry, parent_key=key, separator=separator)

        # базовый случай — кладём значение
        else:
            result[parent_key] = entry

    flatten(data)
    return result
