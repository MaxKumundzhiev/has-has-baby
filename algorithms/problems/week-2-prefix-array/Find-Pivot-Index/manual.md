

**https://leetcode.com/problems/find-pivot-index/description/**

## правильное решени
```python
# memory optimized solution
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        rightSum, leftSum = totalSum, 0
        
        for idx, currentValue in enumerate(nums):
            rightSum -= currentValue
            if rightSum == leftSum:
                return idx
            else:
                leftSum += currentValue
        return -1

# acceptable solution

```

## оценку по времени и памяти
- Time: O(n)
- Space: O(1)

## путь по которому вы пришли к решению
Сразу пришел к правильному концептуальному решению. При реализации, описался и не заметил, что в enumerate передаю range(len(nums)), также, подумал, что добавление нуля в начало поможет обойти крайний случай слева, поэтому еще в enumerate писал, что начинаем с первого индекса. В итоге со второго раза, поправив все недочеты прошло решение.

## идея
Посчитать сумму всех элментов за один проход. Далее, используя эту сумму, считать сумму слева и справа, также проверяя равны ли эти суммы - если да, значит мы нашли крайний левый опорный индекс, если нет, то сначала обновляем сумму слева, потом обновляя сумму справа.