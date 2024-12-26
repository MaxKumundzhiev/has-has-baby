**https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/**

## правильное решени
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def to_bst(self, array: list[int], left: int, right: int):
        # while composing bst, define base case
        # base case, its when left and right pointers overlapped
        # meaning we reach termination leaf (node)
        """
        array = [-2,4,6,12,18,21]
                  0 1 2 3  4  5
                 || 
                 rl 
                  |
                  m
        middle = (l+r) // 2
        """
        if left > right: return
        
        # compose middle between left and right pointers
        # create a node based on middle idx value
        middle = (left + right) // 2
        node = TreeNode(array[middle])

        # recursivly compose left subtree
        # when creating left subtree -- moving right pointer 
        node.left = self.to_bst(array=array, left=left, right=middle-1)
        # recursivly compose right subtree
        # when creating right subtree -- moving left pointer
        node.right = self.to_bst(array=array, left=middle+1, right=right)
        return node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.to_bst(array=nums, left=0, right=len(nums)-1)
```

## оценку по времени и памяти
- Time  O(n)
- Space O(h)

## идея
```text
свойство сбалансированноего дерева:
- когда для каждого поддерева верно утверждение, что высота левого и правого поддерева отличается не более чем 1 (asb(leftTreeHeight - rightTreeHeight)) ≤ 1

идея
мы вспомнили свойство сбалансированного дерева. далее, нам нужно из массива такое дерево построить, соответсвенно, нужно оперировать вершинами из массива. воспользуемся идеей двух указателей и середины. мы найдем середину - что будет нашим корнем. Левее середины будут находиться значения левого поддерева, а правее, нашего правого поддерева. мы построим рекурсивную функцию - которая будет рекурсивно строить левое и правое поддеревья. в функции нам понадобиться определение базового случая - что будет left > right - что значит мы дошли до конца какой то из веток. теперь остается понять как двигать указатели. когда будем работать с левым поддеревом, будем перерассчитывать середину и двигать правый указатель на middle - 1. А когда будем работать с правым поддеревом - будем перерассчитывать середину и двигать левый указатель на middle + 1. Таким образом мы рекурсивно сможем построить дерево.

заметка
- дан отсортированный по возрастанию целочисленный массив
- нужно построить сбалансированное по высоте двоичное дерево
- base case: left > right: return None
- middle idx: (left + right) // 2
- recursive compose left and right nodesL
    node.left = self.foo(array, left=left, right=middle-1)
    node.right = self.foo(array, left=middle+1, right=right)
```