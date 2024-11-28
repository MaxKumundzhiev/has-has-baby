**https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=binary-search**

## правильное решени
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left
```

## оценку по времени и памяти
- Time: O(log(n))
- Space: O(1)

## идея
```text
task might be defined as find closest to target

t=5
T T T F
1 3 5 6
0 1 2 3 4
    | |
    L R
return left
m = 4 + 0 // 2 = 2

val <= target

T F F F
1 3 5 6   t=2
L R

 |
1 3 5 6 t=2
T F F F

     |
1 3 5 6 t=5
T T T F

       |
1 3 5 6   t=7
T T T T F

       |
1 3 5 6   t=0
T T T T
```