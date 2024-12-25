**https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=company&envId=yandex&favoriteSlug=yandex-all**

## правильное решени
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        visited, queue = [], [root]

        if not root:
            return visited
        
        # while queue is not empty
        # means we can pop from the queue
        while queue:
            rightSideNode = None
            nodes_at_level = len(queue)
            for _ in range(nodes_at_level):
                node = queue.pop(0)
                if node:
                    rightSideNode = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightSideNode:
                visited.append(rightSideNode.val)
        return visited
```

## оценку по времени и памяти
- Time  O(n)
- Space O(n) -- remember, for queue it might be used doubly linked list, to make pop and push for O(1)

## идея
Use BFS traversal (alternatively, its called level order traversal). For BFS we use FIFO queue.
Инициализируем пустой visited и queue с root. Используем BFS traversal, где на каждой итерации, **декларируем пустой rightMostNode**, далее, как в стандартном BFS, замеряем кол-во нод на уровне, запускаем цикл по кол-ву нод на уровне, добавляя детей в конец очереди и обновляя **rightMostNode** (в конце самая правая нода будет действительно самой правой).