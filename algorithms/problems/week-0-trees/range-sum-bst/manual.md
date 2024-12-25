**https://leetcode.com/problems/range-sum-of-bst/description/**

## правильное решени
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, node: TreeNode, low: int, high: int) -> int:
        if not node:
            return 0  # Base case: return 0 for null nodes
        
        totalSum = 0
        if low <= node.val <= high:
            totalSum += node.val  # Include node value if it's in the range
        
        # Recurse on left and right subtrees, and add their sums
        totalSum += self.traverse(node.left, low, high)
        totalSum += self.traverse(node.right, low, high)
        
        return totalSum

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0  # Edge case: empty tree
        return self.traverse(root, low, high)
```

## оценку по времени и памяти
time - Time O(n)
space - Time O(h)

## идея
полуемся peorder обходом, на каждой итерации, мы контролируем totalSum, проверяя если нода в рендже.