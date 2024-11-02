"""source: https://www.youtube.com/watch?v=2E54GqF0H4s&list=PLDV1Zeh2NRsDH5Wq-Vk5tDb8gH03cULZS"""

## What is Hash Table and Hash Function
- A hash table is a data structure providing a mapping from keys to values by technique called hashing.
- A hash function H(x) is a function that maps a key `x` to a whole number in a fixed range.
```json
Ideally, we would like to have a very fast insertion, lookup and removal time for the data we are placing within our hash table.

Remarakbly, we can achieve all this in O(1)* time using a hash function as the way to index into hash table.
*The constant time behaviour attributed to hash tables is only true if you have a good uniform hash function.
```

### Constraints of Hash Table
- Keys should be unique and values might be duplicated
- Keys should be hashable
    - In Python, any immutable object (such as an integer, boolean, string, tuple) is hashable, meaning its value does not change during its lifetime

## Properties of Hash Function
1. if `H(x) = H(y)`, then objects `x` and `y` `might be equal`, but if `H(x) != H(y)`, then objects are `certainly` not equal.
```json
Q: How can we speed up this to our advantage to speedup objects comparison?
A: This means that instead of comparing x and y directly, a smarter appraoch is to compare their hash values, and only if they equal, we need to explicetly compare their values.
```
2. a hash function `H(x)` must be `deterministic`
```json
this means if H(x) = y it always must produce y
```
3. we try to uniform hash functions to minimize the number of `hash collisions`

## How does a Hash Table Work
Think of a hash table as an `indexable` block of memory (an array) and we can only access its entries using the value given to us by our hash function H(x).
```
Assume a hash function H(x) = x^2 + 3 mod 10
** result of hash function is an index where we will insert a key:value pair

-------------------------------
idx     key     value
-------------------------------
0       
1
2       2       "byte-eater"
3
4       1       "will.first"
5
6
7       32      "Lauer456"
8
9
-------------------------------
```

### Interesting applications
- compare context of 2 files --  called checksum

## Collision resolution methods (2 most popular)
- separate chaining
```text
deals with hash collisions by maintaining a data structure (usually a linked list) to hold all the different values which hashed to a particular value
``` 
- open addressing
```text
deals with hash collisions by finiding another place within the hash table for the object to go by offsetting it from the position to which it is hashed
``` 

## Complexity analysis
- insertion: avarage O(1)
- lookup: avarage O(1)
- deleting: avarage O(1)
