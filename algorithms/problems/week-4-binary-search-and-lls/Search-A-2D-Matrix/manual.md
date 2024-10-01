**https://leetcode.com/problems/search-a-2d-matrix/description/**

## правильное решени
```python
class Solution:
    def is_good(self, number: int, target: int) -> bool:
        return number <= target
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            left, right = 0, len(row)
            while right-left > 1:
                middle = (right+left) // 2
                good = self.is_good(number=row[middle], target=target)
                if good:
                    left = middle
                else:
                    right = middle
            last_good = row[left]
            if last_good == target:
                return True
            elif last_good > target:
                return False
            else:
                continue
```

## оценку по времени и памяти
- Time: O(log(n*m))
- Space: O(1)

## путь по которому вы пришли к решению
Сразу понял, что нужно итерироваться по строкам матрицы и для каждоый строки применять бинарный поиск.
После, подумал о том, какая будет функция good - и пришел к тому, что функция будет искать ближайший жлемент к таргету и этот ближайший элемент будет находиться в левом индексе. Далее, подумал о том, что нужно проверить, если найденный последний хороший элемент (на левой позции) нужно проверить на равенство с таргетом. Также, добавил условие, что если последний хороший жлемент больше таргета, значит останавливаем поиск, так как по услвовию, последующие строки будут содерджать только большие элементы.   

## идея
Итерироваться по строкам в матрице и для каждой строки применять бинарный поиск, ищя самый близкий к таргету элменет.
Также, воспользоваться свойством, если найденный элменет в строке больше, чем таргет, значит можно останавливать поиск.
