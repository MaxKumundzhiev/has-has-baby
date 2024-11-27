**https://leetcode.com/problems/sqrtx/**

## правильное решени
```python
class Solution:
    # time: O(log n)
    # mem:  O(1)
    def mySqrt(self, x: int) -> int:
        def good(i: int):
            return i * i <= x

        # Note: работаем именно с целыми числами
        # если работать с не целыми, то получим неточный ответ
        # из-за накаплавающейся неточности во float
        l, r = 0, x + 1
        while r - l > 1:
            m = (l + r) // 2
            if good(m):
                l = m
            else:
                r = m
        return l
```

## оценку по времени и памяти
- Time: O(log(n))
- Space: O(1)

## идея
```text
idea
    compose an array from 0 to x including # we know our target is somewhere in the array
    to look up target, we might use binary search
```