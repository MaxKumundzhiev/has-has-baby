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
        if not root:
            return False
        
        mosttLeft = self.mostLeftValue(root)
        mosttRight = self.mostLeftValue(root)
        return minVal <= mosttLeft <= mostRight <= maxVal
```

## оценку по времени и памяти
- Time O(n) - в худшем случае нужно обойти все вершины
```text
         10
         /  \
      2     3
     /         \
   1           4
  /              \
 0               5
```
- Space O(1) - так как не рекурсивно реализуем


## идея
```text
BST свойста
- левее нода меньше
- правее нода больше
- нода должна быть в интервале low < node.val < high
- самое минимально значение хранится в самой левой ноде дерева
- самое максимальное значение хранится в самой правой ноде дерева

идея для наивного решения
впринципи мы можем взять любой обход, скажем в глубину, и проверять на каждой ноде входит ли значение в диапозон. так можно, но это будет неэффективно, так как нужно будет обойти все ноды - то есть, мы не воспользуемся тем, что нам дано бинарное дерево поиска.

идея для оптимального решения
обходить будем не рекурсивно. пользуясь свойством BST - самое минимальное значение хранится в самой левой вершине и самое большое в самой правой вершине - мы можем их найти, просто итеративно спускаясь влево и вправо до конца:
mostLeft
—————————————
current = node
while node.left:
    current = current.left
—————————————
mostRight
—————————————
current = node
while node.right:
    current = current.right
—————————————
и после  проверить что они вписываются в диапозон:
minVal ≤ mostLeft ≤ mostRight ≤  maxVal
```