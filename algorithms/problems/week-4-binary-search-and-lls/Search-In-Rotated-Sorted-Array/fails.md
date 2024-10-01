```python
"""
- find shift
- apply binary search with known shift value

4 5 6 7 0 1 2
      | 
"""

class Solution:
    def is_good_shift(self, number: int, target: int) -> bool:
        return number > target
    
    def is_good(self, number: int, target: int) -> bool:
        return number <= target

    def search_shift(self, array: list[int]) -> int:
        left, right, target = 0, len(array), array[-1]
        while (right-left) > 1:
            middle = (right+left) // 2
            good = self.is_good_shift(number=array[middle], target=target)
            if good:
                left = middle
            else:
                right = middle
        return right

    def search(self, nums: List[int], target: int) -> int:
        shift = self.search_shift(array=nums)
        left, right = shift, len(nums) + shift
        while (right-left) > 1:
            middle = (right+left) // 2
            good = self.is_good(number=nums[middle]%len(nums), target=target)
            if good:
                left = middle
            else:
                right = middle
        return True if nums[left]%len(nums) == target else False
```