**https://leetcode.com/problems/merge-two-sorted-lists/description/**

## правильное решени
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time O(n)
# Space O(n), because we introduce merged Linked List of the length == n
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        current = dummy = ListNode()
        up, down = list1, list2
        while up and down:               
            if up.val <= down.val:
                current.next = up
                up, current = up.next, up
            else:
                current.next = down
                down, current = down.next, down
        if up or down:
            current.next = up if up else down
        return dummy.next
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(n) | O(1)?

## путь по которому вы пришли к решению
Сразу понял, что нужно использовать 2 указателя и + 1 связный список, куда будем добавлять наименьшее из 2 числел. Также сразу понял, как нужно двигать указатели (наименьший). Также сразу понял, что новый список должен быть инициализирован с пустой головой и нужно срхранить ссылку именно на голову, так как по итогу мы окажемся в хвосте.

## идея
2 указателя на начало обоих списков + создать новый список куда будем добавлять элменеты. условие траверса: наименьший добавляется в новый список и наименьший двигается на 1:
    - if up.val <= down.val --> add = up;   up = up.next
    - else                  --> add = down; down = down.next

Также, не забыть, что в конце останется кусок из какого то из списков, поэтому проверяем, что нужно также добавить
    - if up is None --> add = down
    - else          --> add = up
И последнее, не забыть вернуть не просто ссылку на dummy head, а именно dummy.next, так как dummy.haed это None
