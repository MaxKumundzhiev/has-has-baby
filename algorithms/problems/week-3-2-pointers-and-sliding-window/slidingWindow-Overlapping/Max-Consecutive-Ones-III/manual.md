**https://leetcode.com/problems/max-consecutive-ones-iii/description/**

## правильное решени
```python
class Solution:
    def longestOnes(nums, k) -> int:
        # Initialize the left and right pointer to -1
        left = right = -1
      
        # Slide the window to the right until the end of the list is reached
        while right < len(nums) - 1:
            right += 1  # Move the right pointer to the right
          
            # If a zero is encountered, decrement k (number of flips allowed)
            if nums[right] == 0:
                k -= 1
          
            # If k is negative, too many zeros have been flipped
            # thus, move the left pointer to the right
            if k < 0:
                left += 1  # Move the left pointer to the right
              
                # If the left pointer is pointing to a zero, increment k
                if nums[left] == 0:
                    k += 1
      
        # The maximum length of subarray with all ones after flipping k zeros is
        # the difference between the right and left pointers
        return right - left
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(1)

## идея
```text
```