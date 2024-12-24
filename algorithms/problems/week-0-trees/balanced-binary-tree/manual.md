**https://leetcode.com/problems/balanced-binary-tree/description/?envType=company&envId=yandex&favoriteSlug=yandex-all**

## правильное решени
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse_from_bottom_to_top(self, node: TreeNode) -> [bool, int]:
        # we supposed traverse from bottom to top
        # checking if subtree is balanced and managing the height

        # base case: if we reach leaf
        # we assume subtree is balanced, height is 0, cause there is nothing
        if node is None:
            return [True, 0]
        
        # traverse to the bottom of left and right subtrees
        leftSubtree = self.traverse_from_bottom_to_top(node=node.left)
        rightSubtree = self.traverse_from_bottom_to_top(node=node.right)
        
        # at each node
        balanced = leftSubtree[0] and rightSubtree[0] and abs(leftSubtree[1] - rightSubtree[1]) <= 1
        # compose height of substree
        height = 1 + max(leftSubtree[1], rightSubtree[1])
        # return if balanced and height
        return [balanced, height]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.traverse_from_bottom_to_top(node=root)[0]
```

## оценку по времени и памяти
- Time  O(n)
- Space O(h)

## идея