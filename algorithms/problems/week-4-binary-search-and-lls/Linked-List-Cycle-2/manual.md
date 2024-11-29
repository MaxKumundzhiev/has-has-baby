**https://leetcode.com/problems/linked-list-cycle-ii/**

## правильное решени
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, visited = head, set()
        while current:
            if current in visited:
                return current
            visited.add(current)
            current = current.next
        return
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(n)

## идея
```text
visited hashset
    define pointer and visited hashset. at each iteration, check if node is in visited. if reach the end of the ll, no cycle, else, there is cycle.
```