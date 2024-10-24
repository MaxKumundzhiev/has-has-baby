**https://leetcode.com/problems/merge-intervals/description/**

## правильное решени
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for current in intervals:
            if not bool(merged):
                merged.append(current)
            else:
                current_left, current_right = current[0], current[1]
                last_left, last_right = merged[-1][0], merged[-1][1]
                intervals_intersect = max(current_left, last_left) <= min(current_right, last_right)
                if not intervals_intersect:
                    merged.append(current)
                else:
                    merged[-1] = [last_left, max(current_right, last_right)]
        return merged
```

## оценку по времени и памяти
- Time O(n*logn(n))
- Space (k), where k amount of overlapping intervals

## путь по которому вы пришли к решению


## идея
- сортируем все интервалы
- создаем массив для результатов
- итерирвуемся по интервалам и проверяем 
    если последний интервал в резултате и настоязий интервал перекаются - обновлеям интервал в резултатие
    иначе просто добавляем интервал в резултата 