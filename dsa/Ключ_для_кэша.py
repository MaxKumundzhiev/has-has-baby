"""
Реализуй простой кэш для функции с помощью словаря.
Кешируй результат по аргументам функции. Аргументы могут быть любыми — числами, строками, списками.

cached_pow(2, 10) → 1024 # считается
cached_pow(2, 10) → 1024 # из кэша

Почему tuple идеален как ключ словаря, а list — нет?
"""

# cache: dict[tuple[int, int], int] = {}


# def cached_pow(val: int, power: int) -> int:
#     if (val, power) not in cache:
#         cache[(val, power)] = val**power
#     return cache[(val, power)]


def memoize(func):
    cache: dict[tuple, int] = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def pow(val: int, power: int) -> int:
    return val**power


@memoize
def add(a: int, b: int) -> int:
    return a + b


print(pow(2, 10))
print(pow(2, 10))
