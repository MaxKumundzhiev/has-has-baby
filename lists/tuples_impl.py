"""
tuple — это структура данных в Python, которая представляет собой неизменяемый (immutable) контейнер объектов.
- Неизменяемость: после создания tuple его содержимое нельзя изменить (добавлять, удалять или модифицировать элементы).
Упорядоченность: элементы хранятся в фиксированном порядке, доступ по индексу гарантирован.
- Разнотипные элементы: tuple может хранить элементы разных типов (int, float, str, bool, и даже другие tuple или списки).
- Hashable (при всех immutable элементах): если все элементы tuple являются хешируемыми, то сам tuple можно использовать как ключ словаря или элемент множества (set).
- Использование: удобно для хранения фиксированных наборов данных, структурированных записей (например, координаты, пары ключ-значение, несколько возвращаемых значений из функции).

Кортежи immutable, поэтому методов для изменения (append, remove, pop) нет.
Можно использовать кортежи как ключи словаря, если все элементы хешируемые.

API
    - count(val)
    - index(val)
    - in
    - concat()
    - len
"""

from typing import TypeVar, Generic, Sequence, Iterator

T = TypeVar("T")


class IndexError(Exception): ...


class ValueError(Exception): ...


class TupleImpl(Generic[T]):
    def __init__(self, values: Sequence[T]) -> None:
        self._container = tuple(values)
        self._size = len(self._container)

    def __len__(self) -> int:
        return self._size

    def __contains__(self, item: T) -> bool:
        for v in self._container:
            if v == item:
                return True
        return False

    def __getitem__(self, idx: int) -> T:
        if idx < 0:
            idx += self._size
        if idx < 0 or idx >= self._size:
            raise IndexError()
        return self._container[idx]

    def __iter__(self) -> Iterator[T]:
        return iter(self._container)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TupleImpl):
            return False
        return self._container == other._container

    def __hash__(self) -> int:
        return hash(self._container)

    def index(self, val: T) -> int:
        for i, v in enumerate(self._container):
            if v == val:
                return i
        raise ValueError()

    def count(self, val: T) -> int:
        cnt: int = 0
        for v in self._container:
            cnt += 1 if v == val else 0
        return cnt


if __name__ == "__main__":
    t1 = TupleImpl([1, 2, 3])
    t2 = TupleImpl([1, 2, 3])
    # print(t[0])
    # print(t.index(1))
    # print(t.count(1))
    # print(t[-1])
    # print(t[-2])
    # for v in t:
    #     print(v)

    print(t1 == t2)
    d = {}
    d[t1] = "val"
    print(type(d))
