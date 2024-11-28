**https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/**

## правильное решени
```python
class Solution:
    def is_good_offset(self, middleValue: int, mostRightValue: int) -> bool:
        return middleValue > mostRightValue
    
    def find_offset(self, nums: List[int]) -> int:
        left, right = -1, len(nums)
        while right - left > 1:
            middle = (left + right) // 2
            is_good = self.is_good_offset(nums[middle], nums[-1])
            if is_good:
                left = middle
            else:
                right = middle
        """
        3 4 5 1 2
            | |
        T T T F F
        """
        return right

    def findMin(self, nums: List[int]) -> int:
        offset = self.find_offset(nums=nums)
        return nums[offset]
```

## оценку по времени и памяти
- Time: O(log(n))
- Space: O(1)

## идея
```text
idea
    - find offset (which is finding the beggining of the sorted array)
    - knowing the offset, i.e. the starting index of the rotated array
    - we might use property array is sorted and just return an item at the offset index
```