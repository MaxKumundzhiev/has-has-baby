**https://leetcode.com/problems/interval-list-intersections/description/**

## правильное решени
```python
class Solution:
    # проверяем пересекаются ли интервалы
    def is_overlapping(self, a, b):
        return max(a[0], b[0]) <= min(a[1], b[1])
    
    # интервалы обязательно должны пересекаться
    def overlap_two_intervals(self, a, b):
        return [max(a[0], b[0]), min(a[1], b[1])]

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        p1 = 0
        p2 = 0
        while p1 < len(firstList) and p2 < len(secondList):
            # если пересекаются - добавляем в ответ
            if self.is_overlapping(firstList[p1], secondList[p2]):
                result.append(self.overlap_two_intervals(firstList[p1], secondList[p2]))
            
            # важно сравнивать именно концы интервалов, а не начало
            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return result
```

## оценку по времени и памяти
- Time: O(n+m), becuase we need to traverse all the intervals in the worst case scenario
- Space: O(k), where k is the amount of overlapping intervals

## путь по которому вы пришли к решению
Самостоятельно + посмотрел разбор как реализрвать.

## идея
- both lists are already sorted (no need to sort)
- 2 pointers, each pointer at start of each list
- traverse by 2 pointers
- if intervals intersect
    - add thier intersection into answer
- move pointer for that interval, whose right value is lowest
