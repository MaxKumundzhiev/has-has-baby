"""
Дан список целых чисел. Найди все уникальные тройки [a, b, c] такие что a + b + c = 0. Порядок внутри тройки не важен, дубликатов быть не должно.

[-1, 0, 1, 2, -1, -4]  →  [[-1, -1, 2], [-1, 0, 1]]
[0, 0, 0]              →  [[0, 0, 0]]
[1, 2, 3]              →  []

Когда применять 2 pointers: массив отсортирован, или нужно найти пару/тройку элементов с условием, или определить есть ли цикл.
"""


def two_sum(arr: list[int], target: int) -> tuple[int, int] | None:
    l, r = 0, len(arr) - 1
    while l < r:
        curr_sum = arr[l] + arr[r]
        if curr_sum == target:
            return (arr[l], arr[r])
        elif curr_sum > target:
            r -= 1  # ✅
        else:
            l += 1  # ✅
    return None


def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    pairs = []
    for i, n in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:  # пропускаем дубликаты
            continue

        res = two_sum(arr=nums[i + 1 :], target=-n)  # ✅ только правая часть
        if res:
            n2, n3 = res
            pairs.append([n, n2, n3])

    return pairs


print(three_sum([-1, 0, 1, 2, -1, -4]))


"""
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # пропуск дубликатов для первого элемента
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            total = nums[i] + nums[l] + nums[r]

            if total == 0:
                result.append([nums[i], nums[l], nums[r]])
                # пропуск дубликатов для второго и третьего
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif total < 0:
                l += 1
            else:
                r -= 1

    return result
"""
