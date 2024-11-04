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
