**https://leetcode.com/problems/range-sum-query-immutable/description/**

## правильное решени
```python
# formula: prefix[right+1] - prefix[left]

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]
        
        currentSum = 0
        for value in self.nums:
            currentSum += value
            self.prefix.append(currentSum)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(n)

## путь по которому вы пришли к решению
Изначально, было понятно, что нужно использовать префиксный массив. Однако, не смог сразу вывести формулу для подчсета суммы интервала. Посмотрел разбор - стало понятно.