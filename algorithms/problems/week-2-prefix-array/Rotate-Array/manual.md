**https://leetcode.com/problems/rotate-array/description/**

## правильное решени
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length, shift = len(nums), k
        shift_length = shift % length
        boundary = length - shift_length
        nums[:] = nums[boundary:] + nums[:boundary]
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(1)

## идея
**rotation - means how many of the elements from the end we will move to the beggining
Рассчитать длину сдвига как остаток от деления сдвига и длины массива, после рассчитав границу между интервалом левым и правым, поменять их местами.

