**https://leetcode.com/problems/validate-binary-search-tree/**

## правильное решени
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, low: int, high: int, node: TreeNode):
        if not node:
            return True
        
        if not (low < node.val < high):
            return False
        
        return self.traverse(low=low, high=node.val, node=node.left) and \
               self.traverse(low=node.val, high=high, node=node.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.traverse(low=float('-int'), high=float('inf'), node=root)
```

## оценку по времени и памяти
- Time  O(n) - нужно в худшем случае обойти все узлы, где n количество узлов
- Space O(h) - нужно в худшем случае обойти все уровни (кол-во уровней log(n))

## идея
- мы знаем свойство, что для каждой вершины в BST: `minVal < currVal < maxVal`
- будет обходить дерево и (1) проверять на свойство (2) при переходе на другой узел обновлять наши границы слева и справа соответсвенно

```
BST свойста
- левее нода меньше
- правее нода больше
- нода должна быть в интервале low < node.val < high

1. завести low (float(”-inf”)), high (float(”+inf”)) интервалы
2. на каждой итерации проверять удовлетворятся ли условие интервала 
low < node.val < high

когда идем влево: обновляем правую границу
когда идем вправо: обновляем левую границу
```