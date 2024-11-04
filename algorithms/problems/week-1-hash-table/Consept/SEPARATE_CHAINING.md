"""source: https://youtu.be/T9gct6Dx-jo?list=PLDV1Zeh2NRsDH5Wq-Vk5tDb8gH03cULZS"""

## What is Separate Chaining
Separate chanining is one of many strategies to deal with hash collisions by maintaning a data structure (usually a linked list) to hold all the different values which hashed to a particular value.

Note: the data structure used to cache the items which hashed to a particular value is not limited to a linked list. Some implementations use one or mixture of: arrays, binary trees, self balancing trees, etc.


```text
**we use an array of linked lists
idx     - the output of hash function
bucket  - singly | doubly linked list

idx     bucket
0       Name: Rai   --> Name: Rayn
        Age: 25         Age: 56

1       Name: Rick
        Age: 62   

2       Name: Leah   --> Name: Lara
        Age: 18          Age: 46
```

## Implmenetation
from typing import List

```python
class Node:
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value
        self.next = None

    def __hash__(self):
        return hash(self.key)

class HashTable:
    def __init__(self, capacity: int = 10, load_factor: float = 0.75):
        self.capacity = capacity
        self.table: List[Node | None] = [None] * self.capacity
    
    def __get_bucket_lenght(self, idx: int) -> int:
        counter = 0
        current = self.table[idx]
        while current:
            counter += 1
            current = current.next
        return counter

    def __get_bucket_idx(self, hash: int):
        return hash % self.capacity

    def insert(self, key: str, value: int) -> None:
        _node = Node(key=key, value=value)
        _hash = hash(_node)
        _idx = self.__get_bucket_idx(hash=hash_)
        _current = _head = self.table[_idx]
        # bucket empty
        if not _current:
            self.table[_idx] = Node(key=key, value=value)
            return
        # bucket not empty
        # traverse to the end of bucket, checking if node exists
        while _current.next:
            # no modifications for bucket
            # node already exists, return
            if _current.key == _node.key and _current.value == _node.value:
                return
            _current = _current.next
        # node doesnt exist, append to the end of bucket
        _current.next = Node(key=key, value=value)
        # update bucket head
        self.table[_idx] = _head
        return
        
    def remove(self, key: str) -> None:
        # check if object exists in bucket eventually
        _exists = self.lookup(key=key)
        if not _exists: return KeyError
        # object exists in certain bucket
        _node = Node(key=key, value=None)
        _hash = hash(_node)
        _idx = self.__get_bucket_idx(hash=hash_)
        _length = self.__get_bucket_lenght(idx=_idx)

        # object resides in head
        if _length == 1:
            self.table[_idx] = None
        # object resides either in the middle or end 
        else:
            _head = self.table[_idx]
            _previous, _current = Node(key=None, value=None), self.table[_idx]
            while _current:
                if _current.key == node.key:
                    _previous.next = _current.next
                # @NOTE: reiterate
                _previous.next = _current
                _current = _current.next
            self.table[_idx] = _head
        return
    
    def lookup(self, key: str) -> boolean:
        _node = Node(key=key, value=None)
        _hash = hash(_node)
        _idx = self.__get_bucket_idx(hash=hash_)
        _current = self.table[_idx]
        if not _current:
            return False
        while _current:
            if _current.key == _node.key:
                return True
            _current = _current.next
        return False
```
