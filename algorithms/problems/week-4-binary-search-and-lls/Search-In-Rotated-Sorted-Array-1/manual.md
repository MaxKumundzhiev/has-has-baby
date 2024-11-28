**https://leetcode.com/problems/search-in-rotated-sorted-array/description/**

## правильное решени
```python
class Solution:
    # time: O(log n)
    # mem:  O(1)
    def findOffset(self, nums: List[int]):
        # good   bad
        # [   |  1 2 3 4 5]
        #   l    r

        #  good        bad
        # [4 5 6 7  |  0 1 2]
        #        l     r
        def good(i: int):
            return nums[i] > nums[-1]

        l, r = -1, len(nums) - 1
        while r - l > 1:
            m = (l + r) // 2
            if good(m):
                l = m
            else:
                r = m
        return r

    # time: O(log n)
    # mem:  O(1)
    def search(self, nums: List[int], target: int) -> int:
        def good(i: int):
            return nums[i] <= target

        # обычный бинарный поиск, но смещаем на offset дополнительно
        offset = self.findOffset(nums)
        l, r = offset, len(nums) + offset
        while r - l > 1:
            # Note: ошибка №1 это делать "m = (l + r + offset) // 2"
            m = (l + r) // 2
            if good(m % len(nums)):
                l = m
            else:
                r = m
        # Note: ошибка №2 это забыть сделать "(l + offset) % len(nums)"
        realLeft = l % len(nums)
        return realLeft if nums[realLeft] == target else -1
```

## оценку по времени и памяти
- Time: O(log(n))
- Space: O(1)

## путь по которому вы пришли к решению
Сразу понял, что нужно воспользоваться двуми ьин поисками, чтобы найти сначала сдвиг, после найти есть ли таргет в оригигальном массиве.

## идея
Найти при сдвиш при помощи бинарного поиска, далее зная сдвиг, применить бинарный поиск для сдвинутого массива.  