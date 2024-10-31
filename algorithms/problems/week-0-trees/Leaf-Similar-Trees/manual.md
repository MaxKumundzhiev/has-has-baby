**https://leetcode.com/problems/leaf-similar-trees/description/**

## правильное решени
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafValues(root, leaf_values):
            if not root:
                return
            
            if not root.left and not root.right:
                leaf_values.append(root.val)
            
            getLeafValues(root.left, leaf_values)
            getLeafValues(root.right, leaf_values)
        
        leaf_values1, leaf_values2 = [], []
        getLeafValues(root1, leaf_values1)
        getLeafValues(root2, leaf_values2)

        return leaf_values1 == leaf_values2
```

## оценку по времени и памяти
- Time  O(n + m), where n and m are amount of nodes in trees
- Space O(h), where h is max trees height 

## путь по которому вы пришли к решению
Самостоятельно

## идея
- traverse each tree and compose leaf array from left to right, collecting all leaf nodes values
- element wise compare elements