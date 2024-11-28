**https://leetcode.com/problems/find-peak-element/description/?envType=problem-list-v2&envId=binary-search**

## правильное решени
```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = -1, len(nums)-1
        while right - left > 1:
            middle = (left + right) // 2
            if nums[middle] < nums[middle+1]:
                left = middle
            else:
                right = middle
        return right
        
```

## оценку по времени и памяти
- Time: O(log(n))
- Space: O(1)

## идея
```text
use binary search to find the first max element in array (we look for middle and neighbouring value). if value in the mid is less than next, all the values before mid are less. so, we are looking for a first value, which does not satisfy the condition - at right idx.
```