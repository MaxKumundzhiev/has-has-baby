**https://leetcode.com/problems/rotate-array/description/**

## правильное решени
```python
# optimized solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length, shift = len(nums), k
        shift_length = shift % length
        boundary = length - shift_length
        nums[:] = nums[boundary:] + nums[:boundary]
```

```python
# naive solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        amount_of_elements = len(nums)
        shift = k
        hash_table = {}

        for current_idx, current_value in enumerate(nums):
            idx_to_shift = current_idx + shift
            if idx_to_shift >= amount_of_elements:
                idx_to_shift = abs(amount_of_elements - idx_to_shift)
            hash_table[idx_to_shift] = current_value
        
        for idx_to_shift, value_to_swap in hash_table.items():
            nums[idx_to_shift] = value_to_swap
        
        return
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(1)

## путь по которому вы пришли к решению


## идея

