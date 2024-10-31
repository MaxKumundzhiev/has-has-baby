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
        def inorder(node: TreeNode) -> int:
            if not node:
                return
            result = self.inorder(node.left)
            if result is not None:
                return result
            nonlocal k
            k -= 1
            if k == 0:
                return node.val
            return self.inorder(node.right)
        return inorder(root)
```

## оценку по времени и памяти
- Time  O(n)
- Space O(h)

## идея
- использовать inorder traverse, чтобы получать элементы в отсортированном порядке
- также использовать счетчик, чтобы не хранить в памяти весь массив
    - как только счетчик будет равен K - возвразаем результат