"""
генератор - это обвертка в виде функции и ключевого слова yield которая возвразает следующий обьект
генератор - shortcut for building iterators.
    Instead of a class with __iter__ and __next__, you write a function with yield. Python automatically turns it into an iterator.
"""


def countdown(start: int):
    while start > 0:
        yield start
        start -= 1


"""
generator inside of class
You can combine both worlds: put a generator function inside a class to make the class iterable cleanly.
"""


class EvenNumber:
    def __init__(self, limit: int) -> None:
        self._limit = limit

    def __iter__(self):
        """instead of returning pointer to object, we use yield inside"""
        curr: int = 0
        while curr <= self._limit:
            yield curr
            curr += 2


if __name__ == "__main__":
    # print([v for v in countdown(5)])
    # l = list(countdown(5))
    # print(l)
    gen = EvenNumber(10)  # 2,4,6,8,10
    for n in gen:
        print(n)

    gen = EvenNumber(10)  # 2,4,6,8,10
    print(iter(gen))
    print(iter(gen))
