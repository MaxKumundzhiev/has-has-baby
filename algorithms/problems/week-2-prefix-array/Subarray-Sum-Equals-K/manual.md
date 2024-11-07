**https://leetcode.com/problems/subarray-sum-equals-k/description/**

## правильное решени
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        currentSum = 0
        result = 0
        for num in nums:
            currentSum += num
            targetSumToLookUpBefore = currentSum - k
            if targetSumToLookUpBefore in prefixSum:
                count = prefixSum.get(targetSumToLookUpBefore)
                result += count
            prefixSum[currentSum] = prefixSum.get(currentSum, 0) + 1
        return result
```


## оценку по времени и памяти
- Time: O(n)
- Space: O(n)

## идея
to utilize currentSum, k and hashmap. currentSum and k stands for counting a prevSum, which we gonna look up in hash map. hash map stands for storing prefixSum:count pair (aka common prefixSum). 

Eventually, we need to traverse an array, accumulating and writing currSum to hashmap, in the meantime, cheking if prevSum (currSum - k) exists in hashmap (if yes, get the amount and add to result). 


