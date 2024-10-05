**https://leetcode.com/problems/reverse-linked-list/description/**

## правильное решени
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
```

## оценку по времени и памяти
- Time: O(N)
- Space: O(1)

## путь по которому вы пришли к решению
Ранее решал задачу, посмотрел разбор для напоминания подхода. 

## идея
Сначала ввести 2 указателя, prev, curr, где prev указывает на None и curr на голову списка. Далее итерироваться пока curr не пустая нода, на каждой итерации:
    - определять next указатель (next = curr.next)
    - сделать операция разворота (curr.next = prev)
    - передвинуть prev указатель, так как он больше не нужен (мы уже развернули ноды) (prev = curr)
    - передвинуть curr указатель на next, так как он больше не нужен (мы уже развернули ноды) (curr = next)
В конце вернуть prev, так как он будет указывать на конец (начало развернутого списка)