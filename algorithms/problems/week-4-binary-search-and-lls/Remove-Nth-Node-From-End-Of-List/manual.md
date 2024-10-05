**https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/**

## правильное решени
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=None, next=head)
        left, right, shift = dummy, dummy, n+1
        # None 1 2 3 4 5
        #  |       |
        #  l       r
        for _ in range(shift):
            right = right.next
        # traverse till the end
        # as a result, left reference will be at the node 
        # right before which is needed to be deleted
        # None 1 2 3 4 5   # if n=2, thus shift=3
        #          |     |
        #          l     r
        while right:
            left = left.next
            right = right.next
        # perform removal
        left.next = left.next.next
        # return next after dummy Node
        return dummy.next
```

## оценку по времени и памяти
- Time: O(N)
- Space: O(1)

## путь по которому вы пришли к решению
Начал думать в сторону 2-х указателей, а именно, fast and slow, чтобы найти середину и последний и после как то воспользоваться знанием про расстояния, но не дркурутил эту мысль и двинулся в сторону 2-х прохождений связного списка.

## идея
В начале добавить к оригинальному связному списку dummy node, прикрепив его к основному списку. Далее, поставить 2 указателя на самое начало и `сдвинуть правый указатель на k+1 (так как dummy node)` - таким образом мы сформировали окно, которым будем двигаться. Двигаем оба указателя, до тех пор, пока правый не выйдет за границу. Как только правый вышел за границу, бы берем левый указатель и производим удаление ноды. Также, по услвоию нужно вернуть голову списка, поэтому в самом начале, добавим указатель на голову (dummy, но возразаем dummy.next).