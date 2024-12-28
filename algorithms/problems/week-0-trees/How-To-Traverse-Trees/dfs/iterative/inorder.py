# https://www.youtube.com/watch?v=g_S5WuasWUE&t=22s

"""
Идея
  для менеджмента порядка обработки будем использовать стек и порядок LIFO
  1. мы будет идти влево до тех пор пока можем (не встретим пустую ноду) и на каждой итерации будем 
  добавлять в стек ноду
  2. как только мы догли до пустой ноды - мы снимаем ноду из стека и процессим ее (последний элемент)
  3. затем мы попробуем пойти в правого ребенка - если там пустая нода - мы снимаем элемент со стека опять 
"""


from typing import Optional

class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.right = None
        self.val = val

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]):
        curr, stack, res = root, [], []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res