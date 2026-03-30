"""
Дан список чисел. Сожми подряд идущие одинаковые элементы в пару (значение, количество).
[1,1,1,2,3,3,1] → [(1,3),(2,1),(3,2),(1,1)]
Подумай: как отслеживать "текущую серию" при обходе списка?

Размышления
    на входе -> всегда гаранитируется минимум 1 пара
    на выходе -> кортеж (число, кол-во)

    завести счетчик
    итерироваться до препоследнего индекса
    сравнивая элмент на текущем и следуещем индексах

    [1,1,1,2,3,3,1] → []
                 |

    if len(arr) > 1:
        cnt = 3
        idx = 7

        if arr[idx] == arr[idx-1]
            cnt += 1
        else:
            res.append(arr[idx], cnt)
            cnt = 1
"""


def compress(arr: list[int]) -> list[tuple[int, int]]:
    if not arr:
        return []

    cnt = 1
    res: list[tuple[int, int]] = []

    for idx in range(1, len(arr)):
        curr, prev = arr[idx], arr[idx - 1]
        if curr == prev:
            cnt += 1
        else:
            res.append((prev, cnt))  # ✅ prev — the streak that just ended
            cnt = 1

    res.append((arr[-1], cnt))  # ✅ always flush the last streak

    return res


if __name__ == "__main__":
    arr = [1, 1, 1, 2, 3, 3, 1]
    print(compress(arr))
