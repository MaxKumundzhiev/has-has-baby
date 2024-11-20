**https://leetcode.com/problems/maximize-distance-to-closest-person/description/**

## правильное решени
```python
class Solution:
    # time: O(n)
    # mem:  O(1)
    def maxDistToClosest(self, seats: List[int]) -> int:
        l = 0
        r = 0
        result = 0
        while l < len(seats):
            # before
            # l
            # 1 1 1 1 0 0 1 1
            # r

            # бежим правым указателем пока в интервале [l, r]
            # находятся все последовательные числа
            while r + 1 < len(seats) and seats[r] == seats[r + 1]:
                r += 1
            # after
            # l
            # 1 1 1 1 0 0 1 1
            #       r

            # обновляем ответ только если в палавающем окне были 0-ли
            if seats[r] == 0:
                # если 0 прижат к стенке слева или справа, т. е.
                # 1 0 0 0
                #   l   r

                # 0 0 0 1
                # l   r
                # то свободных мест будет r - l + 1 т к посадим в самый край
                if l == 0 or r == len(seats) - 1:
                    result = max(result, r - l + 1)
                # в данном случае окно распологается между 1-ами:
                # 1 0 0 0 1
                #   l   r
                # поэтому находим число мест по формуле (r - l + 2) // 2
                else:
                    result = max(result, (r - l + 2) // 2)

            # интервалы не пересекаются, поэтому сдвигаем
            # на r + 1 - именно отсюда будет начинаться
            # следующий интервал
            l = r + 1
            r = r + 1
        return result
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(1)

## идея
non-ovelapping windows technique.