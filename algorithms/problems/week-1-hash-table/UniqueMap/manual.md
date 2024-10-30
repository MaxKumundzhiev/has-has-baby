**private**

## условие
Реализовать структуру данных UniqueMap
```python
class UniqueMap:
    def __init__(self) -> None:
        ...
    
    # Time O(1)
    def set(self, key: int, val: int) -> None:
        """присваеваем ключу значение. если такой ключ есть. то перезаписываем значение"""
        ...
    
    # Time O(1)
    def remove(self, key: int) -> None:
        """удаляем по ключу значение"""
        ...

    # Time O(1)
    def get(self, key: int) -> int:
        """получаем по ключу значение"""
        ...

    # Time O(1)
    def isAllUnique(self, key: int) -> bool:
        """возвразает true, если никакие 2 ключа не имеют одинаковые значения"""
        ...
```

## правильное решени
```python
class UniqueMap:
    def __init__(self):
        self.key_to_val = {}  # Словарь для хранения пар ключ-значение
        self.val_to_keys = {}  # Словарь для хранения множества ключей для каждого значения

    def set(self, key: int, val: int) -> None:
        # Remove the old key-value pair if it exists
        if key in self.key_to_val:
            old_val = self.key_to_val[key]
            self.val_to_keys[old_val].remove(key)
            if not self.val_to_keys[old_val]:
                del self.val_to_keys[old_val]

        # Add the new key-value pair
        self.key_to_val[key] = val
        self.val_to_keys.setdefault(val, set()).add(key)

    def remove(self, key: int) -> None:
        if key in self.key_to_val:
            val = self.key_to_val[key]
            del self.key_to_val[key]
            self.val_to_keys[val].remove(key)
            if not self.val_to_keys[val]:
                del self.val_to_keys[val]

    def get(self, key: int) -> int:
        return self.key_to_val.get(key, None)

    def isAllUnique(self, key: int) -> bool:
        # Checks if the value associated with the given key is unique.
        val = self.key_to_val.get(key)
        if val is None:
            return False  # Key doesn't exist
        return len(self.val_to_keys[val]) == 1
```

## идея
To use mapping hashmap of form key:value and uniqueness hashmap of form value:allKeys