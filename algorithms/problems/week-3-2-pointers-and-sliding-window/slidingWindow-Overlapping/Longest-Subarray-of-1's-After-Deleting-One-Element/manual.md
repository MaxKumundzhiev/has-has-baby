**https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/**

## правильное решени
```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroCount = 0
        longestWindow = 0
        start = 0

        for idx in range(len(nums)):
            if nums[idx] == 0:
                zeroCount += 1
            
            while zeroCount > 1:
                zeroCount = zeroCount - 1 if nums[start] == 0 else zeroCount
                start += 1
            
            longestWindow = max(longestWindow, idx-start)
        
        return longestWindow
```

## оценку по времени и памяти
- Time: O(s)
- Space: O(1)

## идея
```text
sliding window, non fixed lenght, overlapping
window state: consequitive ones or 0-s == 1
```