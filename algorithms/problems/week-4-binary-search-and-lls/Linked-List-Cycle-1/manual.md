**https://leetcode.com/problems/linked-list-cycle/description/**

## правильное решени
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(1)

## идея
```text
There are 2 approaches: using visited hashset and using fast and slow algorithm

visited hashset
    define pointer and visited hashset. at each iteration, check if node is in visited. if reach the end of the ll, no cycle, else, there is cycle.

fast and slow algorithm
    define 2 pointers, slow and fast. slow moves at 1 pos and fast at 2 pos at a time. according to the math, if there is a cycle, fast will reach slow for n-1 iterations, showing there is a cycle. otherwise, if fast reach the end of ll, there is no cycle.
```