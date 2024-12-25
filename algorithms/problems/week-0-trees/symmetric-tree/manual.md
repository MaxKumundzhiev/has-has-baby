**https://leetcode.com/problems/symmetric-tree/description/?envType=company&envId=yandex&favoriteSlug=yandex-all**

## правильное решени
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, left: TreeNode, right: TreeNode) -> bool:
        # reach termination leaf
        if not left and not right:
            return True
        # intermidiatry node (left and right)
        # if one of the nodes is None - not symmetric
        if not left or not right:
            return False
        # otherwise node has both left and right children
        # compare their values
        # case when values not symmetric - pop up with False
        if left.val != right.val:
            return False
        else:
            return self.traverse(left=left.left, right=right.right) and self.traverse(left=left.right, right=right.left)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(left=root.left, right=root.right)
```

## оценку по времени и памяти
time - Time O(n)
space - Time O(h)

## идея
будем на каждой итерации сравнивать противоположенных детей левого и правого поддеревьев, запустив dfs на левое и правое деревья