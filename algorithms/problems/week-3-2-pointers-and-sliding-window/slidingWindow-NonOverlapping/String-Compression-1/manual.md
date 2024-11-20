**https://leetcode.com/problems/string-compression/description/**

## правильное решени
```python
class Solution:
    # time: O(n)
    # mem:  O(n), если сразу модифицировать массив chars то получим O(1)
    def compress(self, chars: List[str]) -> int:
        l = 0
        r = 0
        result = []
        while l < len(chars):
            # before
            # l
            # a a a b b a a
            # r

            # бежим правым указателем пока в интервале [l, r]
            # находятся все одинаковые символы
            while r + 1 < len(chars) and chars[r] == chars[r + 1]:
                r += 1
            # after
            # l
            # a a a b b a a
            #     r

            # обновляем ответ
            windowSize = r - l + 1
            if windowSize == 1:
                result.append(chars[r])
            else:
                result.append(chars[r])
                result += list(str(windowSize))

            # интервалы не пересекаются, поэтому сдвигаем
            # на r + 1 - именно отсюда будет начинаться
            # следующий интервал
            l = r + 1
            r = r + 1

        for i in range(len(result)):
            chars[i] = result[i]

        return len(result)
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(n)

## идея
sliding window, non overlapping windows. traverse string with l and r pointers, accumulating group of repeating chars and counting group lenght. 
Once group is done, add group meta info to result (or modify an input) and move l and r pointers (both to the r position + 1).