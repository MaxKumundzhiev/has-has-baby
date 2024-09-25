**https://leetcode.com/problems/squares-of-a-sorted-array/description/**

## правильное решени
```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        result = [0] * len(nums)
        positionToInsert = -1
        
        while left <= right:
            leftVal, rightVal = abs(nums[left]), abs(nums[right])
            if rightVal > leftVal:
                result[positionToInsert] = rightVal**2
                right -= 1
            elif rightVal < leftVal:
                result[positionToInsert] = leftVal**2
                left += 1
            else:
                result[positionToInsert] = leftVal**2
                left += 1
            positionToInsert -= 1
        return result
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(n)

## путь по которому вы пришли к решению
Решал утром! Сначала подумал про два указателя, по каждому на конец, сообразил про модуль и сравнение чисел между друг другом, однако, пытался сделать замену инплэйс, что привело меня в тупик. Далее, также остался с подходом двух указателей, только теперь попробовал делать все те же действия через fast and slow указатели, также зашел в тупик. Потом подумал об префиксном подходе - тоже особо ничего не вышло. После посмотрел видео разбор - понял, что упустил главный момент, как мы двигаем указатели и в каком порядку вставляем элменты.

## идея
Два указателя, на начало и конец по каждому, также заолоцировать результирующий массив и индекс вставки с конца. Далее итерируеся, пока указатели не пересекутся, где на каждой итерации сравниваем по модулю числа, вставляем большее число (его квадрат) в конец результирующего. Если вдруг числа равны по модулю, берем любое.
