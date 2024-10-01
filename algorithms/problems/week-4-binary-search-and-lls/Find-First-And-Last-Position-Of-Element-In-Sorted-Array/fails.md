```python
class Solution:
    def good_for_start(self, number: int, target: int):
        return number < target
    
    def good_for_end(self, number: int, target: int):
        return number <= target

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        answer = [-1, -1]
        
        if len(nums) == 0:
            return answer

        left, right = 0, len(nums)
        while right-left > 1:
            middle = (right+left) // 2
            is_good = self.good_for_start(number=nums[middle], target=target)
            if is_good:
                left = middle
            else:
                right = middle
        start_value, start_idx = nums[right], right

        left, right = -1, len(nums)-1
        while right-left > 1:
            middle = (right+left) // 2
            is_good = self.good_for_end(number=nums[middle], target=target)
            if is_good:
                left = middle
            else:
                right = middle
        end_value, end_idx = nums[left], left

        if start_value == target and end_value == target:
            return [start_idx, end_idx]
        else:
            return answer
```