"""https://leetcode.com/problems/binary-tree-inorder-traversal/description/"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self, node, result):
        if not node:
            return

        self.traverse(node.left, result)
        result.append(node.val)
        self.traverse(node.right, result)
        return

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traverse(root, result)
        return result