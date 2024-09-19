**https://leetcode.com/problems/monotonic-array/submissions/1393923804/**

## правильное решени
```python
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # идея в том, что нам не важно монотонно возрастает массив
        # или монотонно убыват, поэтому мы заводим 2 флага:
        # на монотонное возрастание и на монотонное убывание
        is_inc = True
        is_dec = True
        for i in range(1, len(nums)):
            is_inc = is_inc and nums[i - 1] <= nums[i]
            is_dec = is_dec and nums[i - 1] >= nums[i]
        return is_inc or is_dec
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(1)

## путь по которому вы пришли к решению
Изначально, я подумал о двух указателях, а именно быстром и медленном, как то итерироваться по массивы, сравнивая значения на быстром и медленном указателях. Так потенциально можно было бы, но я при реализации начал путаться.

Следующее, о чем я подумал, это ввести переменную возрастания или убывания монотонности, пройтись while циклом до тех пор, пока не поймем возрастает или убывает, но застопорился на дублирующизся элементах.

Далее, посмотрев разбор, понял, что можно сделать два флага, а не один. Начал реализовывать, но запутался снова. Со второй попытки и посмотрев эталонное решение - реализовал задачу.