**https://leetcode.com/problems/valid-perfect-square/description/**

## правильное решени
```python
class Solution:
    def is_good(self, value, num: int) -> bool:
        return value*value <= num
    
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        left, right = 0, num
        while right - left > 1:
            middle = (left + right) // 2
            is_good = self.is_good(middle, num)
            if is_good:
                left = middle
            else:
                right = middle
        return left*left == num
```

## оценку по времени и памяти
- Time: O(log(n))
- Space: O(1)

## идея
```text
find value, whose square is <= then target
answer on the L idx
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
T T T T F F F F F F F F F ...
      | |
      L R

idea
    - find value, which gives in square a number
    - return if found value*value == target
```