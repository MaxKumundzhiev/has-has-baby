**https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/**

## правильное решени
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            currSum = sum(numbers[l], numbers[r])
            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return [l+1, r+1]
        return -1
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(1)

## идея
```text
2 pointers, pointer to start and end
traverse until pointer overlap
on each iteration, check 
    if sum of numbers are == target
        return l+1, r+1
    if currSum > target:
        r -= 1 
    elif currSum < target:
        l += 1
    else:
        return [l+1, r+1]
    return -1
```
