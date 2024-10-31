**private**

## условие
Дан корень бинарного дерева поиска root и minVal c maxVal. Нужно проверить, что для каждой вершины node в дереве выполняется minVal <= val <= maxVal.

## правильное решени
```python
class Solution:
    def mostLeftValue(self, root) -> int:
        current = root
        while current.left:
            current = current.left
        return current.val

    def mostRighttValue(self, root) -> int:
        current = root
        while current.right:
            current = current.right
        return current.val
    
    def main(self, root, minVal, maxVal):
        mosttLeft = self.mostLeftValue(root)
        mosttRight = self.mostLeftValue(root)
        return minVal <= mosttLeft <= maxVal and minVal <= mostRight <= maxVal
```

## оценку по времени и памяти
- Time  O(n)
- Space O(1)

## идея
- найти самый левый узел, так как он будет хранить наименьшее значение
- найти самый правый узел, так как он будет хранить наибольшее значение
- проверить неравенство