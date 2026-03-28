"""
we need to implement data structure list with following api
    - copy
    # adding
    - append(item)
    - extend(iterable)
    - insert(index, item)

    # removing
    - remove(value)
    - pop(index)
    - clear()
    - del

    # Access & Search
    - index(value) - Returns the index of the first occurrence of a specified value.
    - count(value) - Returns the number of occurrences of a specific value.
    - in - Checks if an element exists in the list (returns True or False)  --> def __contains__(self, item: T)

    # Manipulation & Utility
    - len() (function)
    - sort()
    - sorted() (function)
    - reverse()
    - min(), max(), sum()

    # Operators
    - Concatenation (+) - Merges two lists into a new, single list.
    - Multiplication (*) - Repeats the list a specified number of times.
"""

from typing import Generic, TypeVar, Iterable, cast, Protocol


class Comparable(Protocol):
    def __lt__(self, other: "Comparable") -> bool: ...


T = TypeVar("T", bound=Comparable)


class IndexError(Exception): ...


class ValueError(Exception): ...


class Array(Generic[T]):
    DEFAULT_CAPACITY_INC_VALUE: int = 2

    def __init__(self) -> None:
        self._capacity: int = 10  # array capacity size
        self._size: int = 0  # array size (idx to insert a value)
        self._container: list[T | None] = [None] * self._capacity

    def __len__(self) -> int:
        """size of array"""
        return self._size

    def __getitem__(self, idx: int) -> T | None:
        """get item by idx"""
        if idx < 0 or idx >= self._size:
            raise IndexError()
        return self._container[idx]

    def __setitem__(self, idx: int, val: T) -> None:
        if idx < 0 or idx >= self._size:
            raise IndexError()
        self._container[idx] = val

    def __repr__(self) -> str:
        return str([self._container[i] for i in range(self._size)])

    def __contains__(self, item: T) -> bool:
        for v in self._container:
            if v == item:
                return True
        return False

    def __resize(self, requested: int = DEFAULT_CAPACITY_INC_VALUE) -> None:
        self._capacity *= requested
        new_container: list[T | None] = [None] * self._capacity
        for i in range(self._size):
            new_container[i] = self._container[i]
        self._container = new_container

    def append(self, val: T) -> None:
        if self._size == self._capacity:
            self.__resize()
        self._container[self._size] = val
        self._size += 1

    def insert(self, idx: int, val: T) -> None:
        """
        Проверяем, что индекс допустим (не меньше 0 и не больше текущей длины)
        Если массив полный, увеличиваем его ёмкость
        Сдвигаем элементы вправо, начиная с конца, чтобы освободить место
        Вставляем новый элемент на нужную позицию
        Увеличиваем размер массива
        """

        if idx < 0 or idx > self._size:
            raise IndexError()

        if self._size == self._capacity:
            self.__resize()

        # shift to right
        for i in range(self._size, idx, -1):
            self._container[i] = self._container[i - 1]

        self._container[idx] = val
        self._size += 1

    def extend(self, iterable: Iterable[T]) -> None:
        """
        динамически проверить если емкость контейнера
        если не хватает --> self.__resize()
        """
        for val in iterable:
            if self._size == self._capacity:
                self.__resize()
            self._container[self._size] = val
            self._size += 1

    def remove(self, val: T | None) -> None:
        """
        look up the idx of val (first occurrence)
        if idx not found --> raise ValueError
        if idx found, move all elements from right to left and set the last element to None (for safety)
        [1, 2, 4, 5, 6, 3, ...]
         0  1  2  3  4  5
               |
        """
        val_found: bool = False
        for i in range(self._size):
            if self._container[i] == val:
                idx = i
                val_found = True
                break

        if not val_found:
            raise ValueError()

        # 2. Сдвиг элементов влево
        for i in range(idx, self._size - 1):
            self._container[i] = self._container[i + 1]

        # 3. Уменьшаем размер и очищаем последний элемент
        self._container[self._size - 1] = None
        self._size -= 1

    def pop(self, idx: int | None = None) -> T | None:
        """
        модифицирует массив и возвращает элемент находящийся по индексу

        проверить если индекс входит в границы массива
        сохранить в отдельную переменную значение по индексу
        сдвинуть массив влево до индекса
        обновить значение на последней позиции на None
        уменьшить размер
        вернуть значение
        """
        if self._size == 0:
            raise ValueError("pop from empty list")
        idx = self._size - 1 if idx is None else idx
        if idx < 00 or idx >= self._size:
            raise IndexError()
        val = self._container[idx]
        for i in range(idx, self._size - 1):
            self._container[i] = self._container[i + 1]
        self._container[self._size - 1] = None
        self._size -= 1
        return val

    def clear(self) -> None:
        """
        удаляет все элементы из массива
        обновляет size
        """
        for i in range(self._size):
            self._container[i] = None
        self._size = 0

    def index(self, val: T) -> int:
        """
        Returns the index of the first occurrence of a specified value.
        """
        for i, v in enumerate(self._container):
            if v == val:
                return i
        raise ValueError(f"{val} not found")

    def count(self, val: T) -> int:
        """Returns the number of occurrences of a specific value."""
        cnt: int = 0
        for v in self._container:
            if v == val:
                cnt += 1
        return cnt

    def sort(self) -> None:
        """сортирует in-place"""
        # берём только реальные элементы (без None)
        data = cast(list[T], self._container[: self._size])
        data.sort()  # type: ignore
        for i in range(self._size):
            self._container[i] = data[i]

    def sorted(self) -> "Array[T]":
        """возвращает отсортированную копию массива"""
        new_arr = Array[T]()
        for i in range(self._size):
            val = cast(T, self._container[i])
            new_arr.append(val)

        new_arr.sort()
        return new_arr

    def min(self) -> T:
        if self._size == 0:
            raise ValueError("min() arg is an empty Array")
        min_ = cast(T, self._container[0])
        for i in range(1, self._size):
            val = cast(T, self._container[i])
            if val < min_:
                min_ = val
        return min_

    def max(self) -> T:
        if self._size == 0:
            raise ValueError("max() arg is an empty Array")
        max_ = cast(T, self._container[0])
        for i in range(1, self._size):
            val = cast(T, self._container[i])
            if val > max_:
                max_ = val
        return max_

    def sum(self) -> T:
        if self._size == 0:
            raise ValueError("sum() of empty Array")
        total = cast(T, self._container[0])
        for i in range(1, self._size):
            val = cast(T, self._container[i])
            total = total + val

        return total


"""
cap = 10
size = 8
len(iterable) = 10

requested = (cap + len(iterable)) * DEFAULT_CAPACITY_INC_VALUE


[1, 2, 3 None None None]
 0  1  2   3   4    5 
idx = 2
val = 99
capacity = 6
size = 3
"""

l = Array[int]()
l.append(1)
l.append(2)
print(l)
l.insert(2, 3)
print(l)
l.insert(0, -10)
print(l)
l.remove(-10)
print(l)
print(l.pop())
print(l)
print(l.pop(0))
print(l)
l.append(5)
l.insert(len(l), 5)
print(l.count(5))
print(5 in l)
l.append(-5)
print(l)
l.sort()
print(l)
print(l.sum())
