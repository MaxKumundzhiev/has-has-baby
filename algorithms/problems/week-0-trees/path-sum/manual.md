**https://leetcode.com/problems/path-sum/**

## правильное решени
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
```

## оценку по времени и памяти
time - Time O(n)
space - Time O(h)

## идея
полуемся peorder обходом, на каждой итерации, мы контролируем sum, вычитая из sum значение ноды. как только мы доходим до листа, мы проверяем, если сумма равна 0;