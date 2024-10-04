****

## правильное решени
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
```

## оценку по времени и памяти
- Time: O(N)
- Space: O(1)

## путь по которому вы пришли к решению
Знал этот паттерн, однако на разборе уточнил, как именно сдвигаем указатели - медленный всегда на один, быстрый всегда на 2.

## идея
В начале оба указателя указывают на голову. Далее начинаем итерироваться пока нода на (1) быстром указателе и (2) на следующй ноде от быстрого указателя -- `являеются` не пустыми (not None). Если условие выполнено, медленный указатель двигаем на 1, а быстрый на 2. В конце возвращаем медленный указатель.