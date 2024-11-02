**https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/**

## правильное решени
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
```

## оценку по времени и памяти
- Time  O(log(n))
- Space O(1)

## идея
- образаем внимание, что входное дерево это - BST (бинарное дерево поиска)
- вспонимаем свойство бинарного дерева поиска - левое поддерево содержит меньшие значения, правое, большие
- также, пользуемся свойством
```
- если p и q > current -> исследуем правое поддерево
- если p и q < current -> исследуем левое поддерево
- иначе случился сплит -> а значит мы нашли наименьшего общего предка
```

В общем, задача сводится к тому, чтобы найти первый сплит