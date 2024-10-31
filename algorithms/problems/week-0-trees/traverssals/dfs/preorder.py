"""https://leetcode.com/problems/binary-tree-preorder-traversal/description/"""
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

        result.append(node.val)
        self.traverse(node.left, result)
        self.traverse(node.right, result)
        return

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traverse(root, result)
        return result