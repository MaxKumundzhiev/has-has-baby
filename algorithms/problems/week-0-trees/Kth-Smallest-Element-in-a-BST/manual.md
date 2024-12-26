**https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/**

## правильное решени
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        result = None

        def traverse(node):
            nonlocal counter, result  # Use nonlocal to access variables from the outer scope
            if not node or result is not None:
                return

            # Inorder traversal: left -> node -> right
            traverse(node.left)

            # Decrement the counter when visiting the current node
            counter -= 1
            if counter == 0:
                result = node.val
                return

            traverse(node.right)

        traverse(root)
        return result
```

## оценку по времени и памяти
- Time - O(n) - обходим в худшем случае все вершины
- Space - O(h) - высота дерева (кол-во рекурсивных вызовов)

## идея
```
свойство inorder для BST
- при inorder обходе (лево —> нода —> право) - мы получаем элементы в возрастающем порядке
- при inorder обходе (право —> нода —> лево) - мы получаем элементы в убывающем порядке

идея для наивного решения
мы можем воспользоваться золотым правилом inorder traversal (лево - нода - право) - а именно, такой обход в BST дает нам упорядоченный по возрастанию массив. После, получив, мы можем вернуть k-ый наименьший элеменет как idx=k-1, так как индексация по условию с 1.

идея для оптимального решения (без хранения массива)
мы можем воспользоваться тем же золотым правилом inorder traversal - а именно, такой обход в BST дает нам упорядоченный по возрастанию порядок, однако мы будем декрементировать k и останавливаться когда k будет равным 0.
```