# Count Sort (сортировка подсчетом)
### Leetcode
https://leetcode.com/problems/sort-an-array/description/

### Условие
Пусть необходимо отсортировать массив из N числел, каждое от 0 до K.

### Идея
Будем считать количество вхождений каждого числа, а затем выводить каждое число столько раз, сколько оно встречалось.

```Важно```
Count sort может быть реализован `2-мя способами`
    - через массив
    - через хэш таблицу

### Оценка
Времени: O(n)
Памяти: O(k), где k количество уникальных элементов

### Реализация (через массив)
```python
class Solution:
    # solution via array of zeros 
    def sortArray(self, nums: List[int]) -> List[int]:
        minval = min(nums)
        maxval = max(nums)
        k = (maxval - minval) + 1
        count = [0] * k

        for now in nums:
            count[now-minval] += 1
        
        nowpos = 0
        for val in range(k):
            for i in range(count[val]):
                nums[nowpos] = val + minval
                nowpos += 1
        return nums
```
