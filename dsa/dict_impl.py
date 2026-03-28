"""
dict - реализация хэш мапы
хэш мэп это ключ значение структура данных (изменяемая)

в виде ключа мы можем использовать хэшируемые обекты (те обекты котораые имеют __eq__ & __hash__ методы - это неизменяемые обьекты)
в качестве значений мы можем хранить люой тип, включая и вложенные хэш мэпы.

реадизуются хэщ мэпы по разному - мы реализуем через список списков;
у мэп отличительной чертой является хэш функция (которая считае позцию бакета где хранится обьект)
у мэп есть проблемы в виде коллизий (есть решения через resize | probing | adding second hash function)
"""

from typing import TypeVar, Generic


K = TypeVar("K")
V = TypeVar("V")


class KeyError(Exception): ...


from typing import TypeVar, Generic, List, Tuple, Iterator

K = TypeVar("K")
V = TypeVar("V")


class DictImpl(Generic[K, V]):
    DEFAULT_CAPACITY: int = 8
    LOAD_FACTOR: float = 0.7

    def __init__(self, capacity: int = DEFAULT_CAPACITY) -> None:
        self._capacity: int = capacity
        self._size: int = 0
        self._buckets: List[List[Tuple[K, V]]] = [[] for _ in range(capacity)]

    # ------------------------
    # utils
    # ------------------------
    def _hash(self, key: K) -> int:
        return hash(key) % self._capacity

    def _resize(self) -> None:
        old_buckets = self._buckets

        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

        for bucket in old_buckets:
            for k, v in bucket:
                self[k] = v  # rehash

    # ------------------------
    # core API
    # ------------------------
    def __len__(self) -> int:
        return self._size

    def __setitem__(self, key: K, value: V) -> None:
        if self._size / self._capacity > self.LOAD_FACTOR:
            self._resize()

        idx = self._hash(key)
        bucket = self._buckets[idx]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

    def __getitem__(self, key: K) -> V:
        idx = self._hash(key)
        bucket = self._buckets[idx]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(key)

    def __delitem__(self, key: K) -> None:
        idx = self._hash(key)
        bucket = self._buckets[idx]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return

        raise KeyError(key)

    def __contains__(self, key: K) -> bool:
        idx = self._hash(key)
        bucket = self._buckets[idx]

        for k, _ in bucket:
            if k == key:
                return True
        return False

    # ------------------------
    # helpers
    # ------------------------
    def get(self, key: K, default: V | None = None) -> V | None:
        idx = self._hash(key)
        bucket = self._buckets[idx]

        for k, v in bucket:
            if k == key:
                return v
        return default

    def keys(self) -> List[K]:
        return [k for bucket in self._buckets for k, _ in bucket]

    def values(self) -> List[V]:
        return [v for bucket in self._buckets for _, v in bucket]

    def items(self) -> List[Tuple[K, V]]:
        return [pair for bucket in self._buckets for pair in bucket]

    def update(self, other) -> None:
        if isinstance(other, DictImpl):
            for k, v in other.items():
                self[k] = v
        else:
            for k, v in other.items():
                self[k] = v

    def clear(self) -> None:
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

    # ------------------------
    # iteration
    # ------------------------
    def __iter__(self) -> Iterator[K]:
        for bucket in self._buckets:
            for k, _ in bucket:
                yield k

    # ------------------------
    # debug
    # ------------------------
    def __repr__(self) -> str:
        items = [f"{k}: {v}" for bucket in self._buckets for k, v in bucket]
        return "{" + ", ".join(items) + "}"


if __name__ == "__main__":
    d = DictImpl()

    d["a"] = 1
    d["b"] = 2
    d["a"] = 100

    print(d)  # {'a': 100, 'b': 2}
    print(d["a"])  # 100
    print("b" in d)  # True

    print(d.keys())  # ['a', 'b']
    print(d.values())  # [100, 2]
    print(d.items())  # [('a', 100), ('b', 2)]

    for k in d:
        print(k)

    d.update({"c": 3})
    print(d)

    del d["a"]
    print(d)
