**https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/**

## правильное решени
```python
class Solution:
    def search_last_target(self, nums: List[int], target: int) -> int:
        # ответ будет находится в элементе указывающим на l
        # поэтому сдвигаем r на 1 вправо, чтобы l мог принимать
        # значения [0, len(nums) - 1] т е от первого и до последнего
        # индекса включительно
        l, r = 0, len(nums)
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] <= target:
               l = m
            else:
               r = m
        return l if nums[l] == target else -1
    
    def search_first_target(self, nums: List[int], target: int) -> int:
        # ответ будет находится в элементе указывающим на r
        # поэтому сдвигаем l на 1 влево, чтобы r мог принимать
        # значения [0, len(nums) - 1] т е от первого и до последнего
        # индекса включительно
        l, r = -1, len(nums) - 1
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] < target:
               l = m
            else:
               r = m
        return r if nums[r] == target else -1


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        l = self.search_first_target(nums, target)
        r = self.search_last_target(nums, target)
        return [l, r]
```

## оценку по времени и памяти
- Time: O(log(n))
- Space: O(1)

## путь по которому вы пришли к решению
Начала с как применить бин поиск один раз и после размышлений, понял, что нужно применить бин поиск 2 раза, соотвественно, придумать 2 разные функции для начала и конца. Также, сразу понял, что можно проверять на существование интервала по проверке равенства значения на старт позиции и таргета. Все реализовал, но запнулся на 2-ом бинпоиске, а именно определения границы.


## идея
Идея - 2 раза бинарный поиск + переиспользовать стандартную реализацию (шаблон) бинарного поиска.
