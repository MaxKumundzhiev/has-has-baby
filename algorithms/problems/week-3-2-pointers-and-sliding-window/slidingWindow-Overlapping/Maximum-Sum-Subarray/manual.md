**https://leetcode.com/problems/maximum-subarray/description/**

## правильное решени
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        maxSum = nums[0]

        for num in nums[1:]:
            currentSum = max(num, num + currentSum)
            maxSum = max(maxSum, currentSum)
            
        return maxSum
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(1)

## идея
establish currSum and maxSum. On each iteration locate whether currSum will be the sum of currSum and current element or just current element. in other words, on each step we locate whether a new value will increase our sum or not, thus such a way we detect max sequential array.

The idea of Kadane’s algorithm is to traverse over the array from left to right and for each element, find the maximum sum among all subarrays ending at that element. The result will be the maximum of all these values


