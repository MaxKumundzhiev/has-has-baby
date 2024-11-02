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
    def toBST(self, nums: List[int], l: int, r: int) -> TreeNode:
        if l > r:
            return None
        
        mid = (l + r) // 2
        node = TreeNode(nums[mid])

        node.left = self.toBST(nums, l, mid - 1)
        node.right = self.toBST(nums, mid + 1, r)
        return node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.toBST(nums, 0, len(nums)-1)
```

## оценку по времени и памяти
- Time  O(n)
- Space O(h)

## идея
- завести 2 поинтера на начало и конец массива
- найти индекс корня дерева (l + r) // 2
- определить ноду (корень) и построить рекурсивно левое и правое поддеревья