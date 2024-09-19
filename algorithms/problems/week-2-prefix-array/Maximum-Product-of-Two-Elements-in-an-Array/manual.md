**https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/**

## правильное решени
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_1, max_2 = max(nums[0], nums[1]), min(nums[0], nums[1])
    
        if len(nums) == 2:
            return (max_1-1)*(max_2-1)
    
        for idx in range(2, len(nums)):
            value = nums[idx]
            if value > max_1:
                max_2 = max_1
                max_1 = value
            elif max_2 < value <= max_1:
                max_2 = value
            else:
                continue
        return (max_1-1)*(max_2-1)
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(1)

## путь по которому вы пришли к решению
Изначально, возникла идея отсортировать массив, взять последние 2 элемента и применить формулу для подсчета ответа. Однако, такле решение работает не оптимально за O(n*logn) по времени и O(n) по памяти.

Далее, возникла оптимальная идея, а именно, пройтись по массиву, в поиске 2-х максимальных элменетов. Добиться этого можно, сначала правильно проинициазировав max_1 и max_2, и далее, начиная с 3-го элемента, проверять, `(1 if)` если очередное число больше верхней границы - тогда переопределить max_1 и max_2, `(2 elif)` если очередное число входит в интервал max_2 < value <= max_1, тогда переопределить max_2.

