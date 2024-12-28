# https://www.youtube.com/watch?v=QhszUQhGGlA

from typing import Optional

class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]):
        ...