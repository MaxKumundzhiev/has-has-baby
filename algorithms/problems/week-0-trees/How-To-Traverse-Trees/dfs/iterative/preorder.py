# https://www.youtube.com/watch?v=afTpieEZXck&t=279s

"""
Идея
  для менеджмента порядка обработки будем использовать стек и порядок 

"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.right = None
        self.val = val

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]):
        curr, stack = root, []
        res = []
        # while node is not termaination or stack is not empty
        while curr or stack:
            # case, when we need to process node
            if curr:
                # since, its preorder 
                # firstly we process node
                res.append(curr.val)
                # secondly, we add right child of the node to the stack
                stack.append(curr.right)
                # move further to the left
                curr = curr.left
            else:
                # pop the last node from stack
                curr = stack.pop()
        return res
