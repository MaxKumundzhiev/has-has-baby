**https://leetcode.com/problems/move-zeroes/description/**

## правильное решени
```python
class Solution:
    # time: O(n)
    # mem: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        # Note: задача может формулироваться как "удалить все 0 из массива"
        # тут смысл такой же, просто делаем resize в конце или попаем (зависит от ЯП)

        slowIdx = 0
        for fastIdx in range(len(nums)):
            if nums[fastIdx] == 0:
                continue
            nums[slowIdx] = nums[fastIdx]
            slowIdx += 1
        
        for idx in range(slowIdx, len(nums)):
            nums[idx] = 0
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(1)

## идея
define slow and fast idx, traverse fast idx until meet non-zero element. at this moment, we assume on a slow idx there will be a zero (pay attention, if not, the elements will be equal same). once updated, move slow idx to the next one.

```text
2 pointers, fast and slow
    fast - should look up first non zero idx, then perform swap
    slow - should look up first zero idx
    traverse until fast idx meet boundary

the position of slowIdx means, on the right side all the elements should be updated to 0
```
