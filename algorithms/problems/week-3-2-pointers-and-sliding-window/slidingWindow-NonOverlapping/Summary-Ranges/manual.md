****

## правильное решени
```python
class Solution:
    # time: O(n)
    # mem:  O(n), без учета памяти на ответ O(1)
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = 0
        r = 0
        result = []
        while l < len(nums):
            # before
            # l
            # 1 2 3 5 7 8
            # r
            
            # бежим правым указателем пока в интервале [l, r]
            # находятся все последовательные числа
            while r + 1 < len(nums) and nums[r] + 1 == nums[r + 1]:
                r += 1
            # after
            # l
            # 1 2 3 5 7 8
            #     r
            # бежим правым указателем

            # добавлем в ответ
            if r != l:
                result.append(f'{nums[l]}->{nums[r]}')
            else:
                result.append(f'{nums[l]}')

            # интервалы не пересекаются, поэтому сдвигаем
            # на r + 1 - именно отсюда будет начинаться
            # следующий интервал
            l = r + 1
            r = r + 1
        return result
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(n)

## идея
sliding window, non overlapping windows