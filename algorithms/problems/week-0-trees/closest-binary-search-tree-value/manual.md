**https://leetcode.com/problems/closest-binary-search-tree-value/description/**

## правильное решени
```python
# property of BST: left subtree nodes will be less than node.val
# property of BST: right subtree nodes will be grater than node.val 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node:TreeNode, target:float, closest:float) -> float | int:
        # base case: termination leaf
        if not node:
            return closest
        
        # compose check to update closest value
        # !!! "closest" if a value of a node, and not a difference itself
        # if current difference (target-node.val) is lower than previous one (target-closest)
        if abs(target-node.val) < abs(target-closest):
            closest = node.val
        # pay attention, it might be a case, i.e: 
        """
        target=4.5; closest=4; current=5
        difference would be euqal: abs(4.5-5) ... abs(4.5-4) --> 0.5 ... 0.5
        in such case, we have to pick the lowest value
        """
        elif abs(target-node.val) == abs(target-closest):
            closest = min(node.val, closest)
        
        # confirm, which way to traverse further, according to BST property
        # if target grater than current value: i.e: 3.71 (target) > 2 (node) 
        # -> we need right subtree, because in the left subtree values are lower, thus difference will be grater
        """
                4
               / \
             `2`   5
             / \
            1   3
        """
        if target > node.val:
            return self.traverse(node=node.right, target=target, closest=closest)
        # if target lower than current value: i.e: 3.71 (target) < 4 (node) 
        # -> we need left subtree, because in the right subtree values are grater, thus difference will be grater
        """
               `4`
               / \
              2   5
             / \
            1   3
        """
        elif target < node.val:
            return self.traverse(node=node.left, target=target, closest=closest)
        return closest

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        return self.traverse(node=root, target=target, closest=float("-inf"))
```

## оценку по времени и памяти
- Time  O(log(n))
- Space O(h)

## идея
```text
свойство BST
левее от ноды - значения меньше
правее от ноды - значения больше

идея
воспользуемся preorder обходом. также нужно воспользоваться свойством BST, проверяя node.val > target | node.val < target. Если таргет больше, чем значение ноды - значит левое поддерево можно не проходить, будем смотреть правое и также, если значение ноды больше, чем таргет, значит правое поддерево не нужно проходить, будем смотреть левое поддерево. также, в каждой ноде, мы будем обновлять ближайшее значение, только с случае, если разница между таргетом и значение ноды будет меньше чем разница между таргутом и последним ближайшим числом по модулю

заметка
- traverse: preorder
- разница считается как: 
    if abs(target-node.val) < abs(target-closest): 
        closest = node.val
    elif abs(target-node.val) == abs(target-closest):
        closest = min(node.val, closest)
- base case:
   if not node:
      return closest
- how traverse with BST property:
   if target > node.val:
      return self.foo(node=node.right) # right subtree contains closer values
   elif target < node.val:
        return self.foo(node=node.left) # left subtree contains closer values
```
