**https://leetcode.com/problems/maximum-average-subarray-i/description/**

## правильное решени
```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = 0
        # composed first window of size k
        for idx in range(k):
            currSum += nums[idx]
        maxSum = currSum

        l, r = 0, k-1
        while r+1 < len(nums):
            leftVal, rightVal = nums[l], nums[r+1]
            currSum += rightVal - leftVal
            maxSum = max(maxSum, currSum)
            l += 1
            r += 1
        return maxSum / k
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(1)

## идея
```text
- range of values -100.000 <= num <= +100.000
- repeated values might be
- fixed size window len of k

k = 3
currSum = 8 - 1 +(-6) = 1
l, r = 1, 3
maxAverage = 8 / 3 = 2.6

1 12 -5 -6 50 3
   |
        |
0 1   2  3 4  5

idea
- sliding window, fixed size
    - edge cases
        - if k > len(nums)
            return -1
        - if k == len(nums)
            return sum(nums) / k
        - if k < len(nums)
            - compose first window of size k
            - set maxAverage = sum(nums) / k
        - traverse
            - on each iteration we add next num and remove first
            - compose and update maxAverage

Time    O(n)
Space   O(1)
           |      |
1 12 -5 -6 50 3 ..
         |    | 
      2 3  4  5 
```