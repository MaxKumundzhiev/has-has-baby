"""
## 3. HashMap
Словарь как вспомогательная структура для быстрого поиска, подсчёта частот или запоминания уже виденного. Превращает `O(n²)` в `O(n)` за счёт `O(n)` памяти.
Когда применять: "видел ли я это раньше", "сколько раз встречается", "какой индекс у элемента X".

**Задача — самый длинный подмассив с равным числом 0 и 1**

Дан бинарный массив (только 0 и 1).
Найди длину самого длинного подмассива с одинаковым количеством нулей и единиц.
```
[0,1]        →  2
[0,1,0]      →  2
[0,1,1,0,1]  →  4  (подмассив [0,1,1,0] или [1,0,1,0] — не важно какой)

Idea (incorrect, duce to conditions)
    we need to find the length of subarray -> thus sliding window
    sliding window - is it fixed size -> no -> thus sliding window with intersected | non intersected answers
    in our case not intersected

    lets see an example
    0 0 0 0 1 0 1 1 1 1 0

    longest gonna be 5 of 1-s
    we gonna use left and right pointer
    accumulate window while sequential number

Idea
    prefix sum + hashmap
    replace 0-s to -1 (to manage whether sum == 0 or not if 0, means this subarray in sum gives 0)
"""

"""
0 0 0 0 1 0 1 1 1 1 1 0
        |
          |

max_len = 0
l = 0
r = 0
"""


def find_max_length(nums: list[int]) -> int:
    # первый раз сумма 0 встречается до начала массива (индекс -1)
    seen: dict[int, int] = {0: -1}
    prefix_sum = 0
    max_len = 0

    for i, n in enumerate(nums):
        prefix_sum += 1 if n == 1 else -1

        if prefix_sum in seen:
            # нашли подмассив с суммой 0
            max_len = max(max_len, i - seen[prefix_sum])
        else:
            # запоминаем первое вхождение этой суммы
            seen[prefix_sum] = i

    return max_len


if __name__ == "__main__":
    assert find_max_length([0, 1]) == 2
    assert find_max_length([0, 1, 0]) == 2
    assert find_max_length([0, 1, 1, 0, 1]) == 4


"""
Пошагово для `[0,1,1,0,1]`:
l=0: [0]→0=1,1=0  [0,1]→0=1,1=1 ✅ len=2  [0,1,1]→0=1,1=2  [0,1,1,0]→0=2,1=2 ✅ len=4
l=1: [1]→0=0,1=1  [1,1]→0=0,1=2  [1,1,0]→0=1,1=2  [1,1,0,1]→0=1,1=3
l=2: [1]→0=0,1=1  [1,0]→0=1,1=1 ✅ len=2  [1,0,1]→0=1,1=2
l=3: [0]→0=1,1=0  [0,1]→0=1,1=1 ✅ len=2
l=4: [1]→0=0,1=1  → max_len = 4
"""
