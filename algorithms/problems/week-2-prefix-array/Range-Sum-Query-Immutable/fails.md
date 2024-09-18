## 1st
```python
attempts:
    1: wrong answer input: [6,5,4,4]

2 pointers
1 3 2
  |

def foo(nums):
    if len(nums) <= 2:
        return True
    
    increasing, decreasing = True, True
    for idx in range(1, range(len(nums))):
        # decreasing
        if nums[idx-1] >= nums[idx]:
            increasing = False
        # increasing
        elif nums[idx-1] <= nums[idx]:
            decreasing = False
        else:
            continue
    
    return True if any(increasing, decreasing) is True
```


## 2nd 
```python
[6,5,4,4]

is_increasing False
is_decreasing True
idx           3
previous      4    
current       4

4 <= 4 and False
4 >= 4 and True


def foo(nums: List[int]) -> bool:
    is_increasing, is_decreasing = True, True
    for idx in range(1, len(nums)):
        previous, current = nums[idx-1], nums[idx]
        
        # increasing array
        if previous <= current and is_increasing is True:
            is_decreasing = False
        
        # decreasing array
        elif previous >= current and is_decreasing is True:
            is_increasing = False
    
    return True if (is_increasing == is_decreasing) == False else False
```