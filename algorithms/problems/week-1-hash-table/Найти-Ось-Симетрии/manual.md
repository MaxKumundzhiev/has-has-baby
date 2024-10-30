**https://leetcode.com/problems/line-reflection/description/**

## правильное решени
```python
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        # находим минимальный и максимальный X
        maxX = max(x for x, y in points)
        minX = min(x for x, y in points)

        # сделали словарь, чтобы проверять наличие точки за O(1)
        points_set = {(x, y) for x, y in points}
        for x, y in points:
            # symX = maxX + minX - x
            # symX - координата точки по оси X симметричной x
            if (maxX + minX - x, y) not in points_set: return False
        return True
```

## оценку по времени и памяти
- Time  O(n)
- Space O(n)

## путь по которому вы пришли к решению
What is symmetric - when distances between 2 points form point to line in between them are equal. There is a formula for counting symmetric point: `maxX + minX - currX`. Keep in mind, symmetric points have equal `y` coordinates (located at the same "line").

## идея
1. find minX, maxX
2. compose frequency hashMap against all points
    key=coordinate
    value=frequency
3. traverse all points
    - count symX by formula: xymX=maxX+minX-currX
    - check if symX in hashMap
    - if no
        - return False
    - if yes
        - check if cnt for currX and symX are equal
        - if no
            - return False    