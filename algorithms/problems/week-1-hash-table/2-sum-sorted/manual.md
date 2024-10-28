**https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/**

## правильное решени
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        offset, left, right = 1, 0, len(numbers)-1
        while left < right:
            sum_ = numbers[left] + numbers[right]
            if sum_ > target:
                right -= 1
            elif sum_ < target:
                left += 1
            else:
                return [left+offset, right+offset]
```

## оценку по времени и памяти
- Time  O(n)
- Space O(1)

## путь по которому вы пришли к решению
Самостоятельно

## идея
```json
2 pointers, from both sides
start traverse 2 pointers until they meet
count sum of numbers at pointers
if sum > target:
    move right pointer
if sum < target:
    move left pointer
else:
    return [idx1, idx2]

[2,7,11,15], target = 9
 | |

left = 0
right = 1
target = 9
sum_ = 13

- idx start from 1
```
