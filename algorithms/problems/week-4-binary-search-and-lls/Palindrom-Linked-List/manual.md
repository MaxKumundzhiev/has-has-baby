**https://leetcode.com/problems/palindrome-linked-list/**

## правильное решени
```python
# Time O(n)
# Space O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle of the linked list
        fast = slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        middle = slow

        # reverse linked list from middle
        prev, curr = middle, middle.next
        # unattach middle from left side
        prev.next = None
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # 2 pointers, traverse from left and right sides towards each other
        left, right = head, prev
        while right is not None and left is not None:
            if left.val != right.val:
                return False
            else:
                left = left.next
                right = right.next
        return True
```

## оценку по времени и памяти
- Time: O(N)
- Space: O(1)

## путь по которому вы пришли к решению
Посмотрел разбор

## идея
Сначала нужно найти середину списка (fast and slow паттерн), далее, нужно развернуть парвую часть от середины в обратную сторону (reverse паттерн), далее необходимо пометить, что middle нода указывает на None, далее необходимо воспользоваться 2 pointers (left and right to start and end) паттерном, и итерироваться навстречу друг другу пока не встретим None, проверяя одинаковые ли занчени в нодах или нет.
