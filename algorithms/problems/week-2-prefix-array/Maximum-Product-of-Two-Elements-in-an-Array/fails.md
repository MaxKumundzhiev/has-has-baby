from typing import List

```json
naive solution

Time O(n*logn)
Space O(n)

Attempts:
- first passed
```

```python
def max_product(array: List[int]) -> int:
        array.sort()
        x, y = array[-1], array[-2]
        return (x-1)*(y-1)
```     

```json
optimized solution

Time O(n)
Space O(1)

Attempts:
- 1 failed (leetcode test: case 2 (input = [1,5,4,5], output = 12, excpected = 16))
    - logic typo with loop: should be range(2, len(nums)), instead had range(2, len(nums)-1)
    
- 2 failed (leetcode test: case 1 (input = [3,4,5,2], output = 16, excpected = 12))
    - incorrect elif (value > max_2) and (value <= max_1):
```

```python
def max_product(nums: List[int]) -> int:
    max_1, max_2 = max(nums[0], nums[1]), min(nums[0], nums[1])  # 4, 3
    
    if len(nums) == 2:
        return (max_1-1)*(max_2-1)
    
    
    for idx in range(2, len(nums)):
        value = nums[idx]    
        if value > max_1:
            max_2 = max_1
            max_1 = value
        elif (value > max_2) and (value <= max_1):
            max_2 = value
    
    return (max_1-1)*(max_2-1)
```