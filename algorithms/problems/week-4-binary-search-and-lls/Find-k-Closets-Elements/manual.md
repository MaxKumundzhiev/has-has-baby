**https://leetcode.com/problems/find-k-closest-elements/**

## правильное решени
```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k

        # Binary search to find the start index of the window
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]
```

## оценку по времени и памяти
- Time: O(log(n))
- Space: O(1)

## идея
Convert the task to find the first most closest element, then use 2 pointers