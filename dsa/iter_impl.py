"""
iterators - итераторы - концепт (протокол) который умеет отдавать следующий обьект.
у него есть два основных метода
    __iter__
    __next__

__iter__ - отдает сам обьект (итератор)
__next__ - отдает следующий элемент или выкидывает ошибку StopIteration - когда элементов не остается
"""

from typing import TypeVar, Generic, Iterable

T = TypeVar("T")


class IteratorImpl(Generic[T]):
    def __init__(self, iterable: list[T]) -> None:
        self._container: list[T] = iterable
        self._index: int = 0

    def __iter__(self) -> "IteratorImpl[T]":
        return self

    def __next__(self) -> T:
        if self._index >= len(self._container):
            raise StopIteration
        val: T = self._container[self._index]
        self._index += 1
        return val


"""
interator, which on count down from start position;
"""


class Countdown:
    def __init__(self, start: int | None = None) -> None:
        self._curr = start

    def __iter__(self) -> "Countdown":
        return self

    def __next__(self) -> int:
        if self._curr is None or self._curr < 0:
            raise StopIteration
        val: int = self._curr
        self._curr -= 1
        return val


if __name__ == "__main__":
    it = IteratorImpl([1, 2, 3, 4])
    for v in it:
        print(v)

    it = IteratorImpl([1, 2, 3, 4])
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))

    cnt = Countdown(10)
    for i in cnt:
        print(i)
