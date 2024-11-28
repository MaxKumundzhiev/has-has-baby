**https://leetcode.com/problems/peak-index-in-a-mountain-array/description/**

## правильное решени
```python
class Solution:
    def is_good(self, val1: int, val2: int) -> bool:
        return val1 > val2

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        T T T T F F F
        1 2 3 4 3 2 1
              | |
              L R
        0 1 2 3 4 5 6
                
        middle = (6 + 3) // 2 = 4
        3 > 1
        """

        left, right = 1, len(arr)-1
        while right - left > 1:
            middle = (left + right) // 2
            is_good = self.is_good(arr[middle], arr[middle-1])
            if is_good:
                left = middle
            else:
                right = middle
        return left
```

## оценку по времени и памяти
- Time: O(log(n))
- Space: O(1)

## идея
```text
- understand, that good function is to compare curr element (at mid) with previous (at mid -1)
- understand, that left idx should start from 1, because answer can not be at 1 idx
```