"""
level order traversal --> its BFS, which is solved using queue
idea
    - declare queue and visisted
    - initialise queue with root
    - while queue is not empty
        - pop from queue mostLeft node
        - add node value to visisted
        - add node left and rigth children to the end of the queue
    return visited
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        visited, queue = [], [root]
        while queue:
            nodes_at_level = len(queue)
            level = []
            for _ in range(nodes_at_level):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            visited.append(level)
        return visited