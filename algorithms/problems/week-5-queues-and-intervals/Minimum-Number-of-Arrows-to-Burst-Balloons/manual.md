**https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/**

## правильное решени
```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        current_, idx = points[0], 1
        shoots = 0

        while idx < len(points):
            next_ = points[idx]
            current_intersects_next = max(current_[0], next_[0]) <= min(current_[1], next_[1])
            if current_intersects_next:
                current_ = [max(current_[0], next_[0]), min(current_[1], next_[1])]
                idx += 1
            else:
                current_ = next_
                shoots += 1
                idx += 1
        shoots += 1
        return shoots
```

## оценку по времени и памяти
- Time: O(n*log(n))
- Space: O(1)

## путь по которому вы пришли к решению
разбор

## идея
- sort the array
- introduce a current array and shoots counter
- start iterating over intervals 
- if current is empty
    - add an interval
- else
    - while next interval intersets
        - update current interval (intersection area)
        - update pointer
    - update counter of shoots
    - update pointer