"""
Скользящее среднее
Напиши функцию, которая принимает список чисел и размер окна k, и возвращает новый список со скользящим средним.
([1,2,3,4,5], k=3) → [2.0, 3.0, 4.0]
Без использования библиотек. Что делать, если k > len(list)?

Размышления
    2 цикла
    1 цикл пройдет от 0 до k
        соберем сумму
    посчитаем среднее

[1,2,3,4,5], k=3) → []
       |

sum_ = 6
"""


def moving_average(arr: list[int], k: int) -> list[float]:
    if not arr or k <= 0 or k > len(arr):
        return []

    window_sum = sum(arr[:k])
    res = [window_sum / k]

    for idx in range(k, len(arr)):
        window_sum += arr[idx] - arr[idx - k]
        res.append(window_sum / k)

    return res


if __name__ == "__main__":
    print(moving_average([1, 2, 3, 4, 5], k=3))
