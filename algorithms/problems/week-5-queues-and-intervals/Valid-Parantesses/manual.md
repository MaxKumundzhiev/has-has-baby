****

## правильное решени
```python
"""
3 types of parantesses: (), {}, []

idea
    - use queue as a container (array)
    - we gonna put open bracket on top of queue (at the end of array)
    - we gonna pop bracket from queue (array) if:
        * queue is not empty AND queue last bracket type is same as clsoing bracket

Time    O(n) + ~O(1)
Space   O(n/2)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        queue: list = []
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        # invalid, cause only 1 bracket is presented
        if len(s) == 1:
            return False
        
        for bracket in s:
            # enqueue
            # opening bracket occurred
            if bracket in mapping:
                queue.append(bracket)
            # dequeue
            # closing bracket occurred
            else:
                # edge case: queue is empty
                # thus we can not perform dequeue
                # might return False right away
                # []        --> bool(queue) --> False
                # [1, 2]    --> bool(queue) --> True
                if not bool(queue):
                    return False
                # edge case: last opening bracket in queue is not equal to current bracket
                # thus we can not perform dequeue
                # might return False right away
                elif mapping.get(queue[-1]) != bracket:
                    return False
                # expected behaviour: last opening bracket in queue is equal to current bracket
                else:
                    _ = queue.pop()
        
        # edge case: perform sanity check in case if 
        # there are reamining opening brackets in queue
        # []        --> bool(queue) --> False
        # [1, 2]    --> bool(queue) --> True
        queue_is_empty = True if bool(queue) is False else False
        return True if queue_is_empty else False
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(n/2), array + hashmap

## путь по которому вы пришли к решению
Раннее решал задачу.

## идея
Нужно использовать очередь как концепт (+ использовать массив + LIFO как структуры данных). Далее, каждый новый элемент мы кладем в очередь, если элемент открывающийся, а если элемент закрывающийся, то проверяем если очередь не пустая и если `тип` этого элмента совпадает с типом последнего элемента в очереди. По окончанию цикла, проверяем сотсояние очереди. Если очередь пустая - последовательность валидно, иначе, нет.
