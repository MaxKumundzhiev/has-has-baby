"""
Окно фиксированного или переменного размера скользит по массиву.
Ключевая идея: не пересчитывать всё окно заново — при сдвиге убираем левый элемент и добавляем правый за `O(1)`.

Когда применять: "найди подмассив/подстроку с условием на длину или сумму".

**Задача — минимальный подмассив с суммой ≥ target**
Дан массив положительных целых чисел и число `target`. Найди минимальную длину подмассива с суммой ≥ target. Если такого нет — верни 0.
```
(target=7, [2,3,1,2,4,3])   →  2  (подмассив [4,3])
(target=4, [1,4,4])         →  1  (подмассив [4])
(target=11, [1,1,1,1,1])    →  0
"""

"""
минимальный подмассив с суммой ≥ target
target=7, [2,3,1,2,4,3]

2,3,1,2,4,3
|   |
  |     |
      |   |
        | |
Idea
    window fixed or not -> no
    answer interected or not -> yes, intersected
    means
        we use 2 pointers, right pointer moves on each iteration one step
        on each iteration we check if window sum >= target
            if yes, we update the lenght and subarray
            shrink left pointer until the condition (window_sum <= target)

2,3,1,2,4,3
|
|
"""


def min_subarray_len(nums: list[int], target: int) -> list:
    l = 0
    curr_sum: int = 0
    min_len: int | float = float("inf")
    result: list[int] = []
    for r in range(len(nums)):
        # accumulate window on each iteration
        curr_sum += nums[r]
        while curr_sum >= target:
            if r - l + 1 < min_len:
                min_len = r - l + 1
                result = nums[l : r + 1]  # сохраняем лучшее окно
            curr_sum -= nums[l]
            l += 1
    return result


if __name__ == "__main__":
    arr = [2, 3, 1, 2, 4, 3]
    target = 7
    res = min_subarray_len(arr, target)
    assert res == [4, 3], f"{res}"
