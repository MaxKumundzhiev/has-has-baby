**private**

## условие
Также как и в https://leetcode.com/problems/range-sum-query-immutable/description/, только нужно найти произведение.

## правильное решени
```python
# formula: prefix[right+1] - prefix[left]

class Solution:
    def __init__(self, nums: List[int]) -> None:
        self.prefix = [1]  # set 1 as a first element
        self.counter = [0]

        # populate prefix array (product of non-zero elements)
        # if zero met, assign previous value
        for num in numbers:
            if num == 0:
                self.prefix.append(self.prefix[-1])
            self.prefix.append(num*self.prefix[-1])
        
        # populate counter array (amount of zeros)
        for num in nums:
            if num != 0:
                self.counter.append(self.prefix[-1])
            self.counter.append(self.prefix[-1]+1)
    
    def product(self, left: int, right: int):
        # formula: array[right+1] / array[left]
        zeroes = self.counter[right+1] - self.counter[left]
        if zeroes > 1:
            return 0
        return self.prefix[right+1] / self.prefix[left]
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(n)

## идея
Завести 2 префиксных массива, 1 для подсчета 0-лей, а второй для подсчета произведения всех не нулевых элементов.