**https://leetcode.com/problems/rotate-array/description/**

## правильное решени
```python
# optimized solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length, shift = len(nums), k
        shift_length = shift % length
        boundary = length - shift_length
        nums[:] = nums[boundary:] + nums[:boundary]
```

```python
# naive solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        amount_of_elements = len(nums)
        shift = k
        hash_table = {}

        for current_idx, current_value in enumerate(nums):
            idx_to_shift = current_idx + shift
            if idx_to_shift >= amount_of_elements:
                idx_to_shift = abs(amount_of_elements - idx_to_shift)
            hash_table[idx_to_shift] = current_value
        
        for idx_to_shift, value_to_swap in hash_table.items():
            nums[idx_to_shift] = value_to_swap
        
        return
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(1)

## путь по которому вы пришли к решению
Сначала возникла идея пройтись по массиву и для каждого элемента посчитать его смещенную позицию,
и класть маппинг в хэш таблицу. Аозникла проблема, что в какой то момент, индексы стали выходить за пределы и нужно было придумать что то с подсчетом таким индексов. 

Далее представив визуально как перемещаются элмементы, я обратил внимание, что я в голове всегда брал как бы правую часть массива и сдвигал ее просто на левую часть. И потом мне пришла идея что нужно находить такой интервал(ы), которые нужно просто поменять местами. Плюс, нужно помнить про то, что сдвиг может превышать размер самого массива. 

## идея
Рассчитать длину сдвига как остаток от деления сдвига и длины массива, после рассчитав границу между интервалом левым и правым, поменять их местами.

