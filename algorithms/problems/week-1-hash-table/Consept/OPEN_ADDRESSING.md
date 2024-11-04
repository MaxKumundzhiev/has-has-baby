"""source: https://youtu.be/xIejolxzZS8?list=PLDV1Zeh2NRsDH5Wq-Vk5tDb8gH03cULZS"""

## What is Open Addressing
When using open addressing as a collision resolution technique, the key-value pairs are stored in a table (array) itself as opposed to a data structure like a separate chaining. This means, we need to care a great deal about the size of our hash table and how many elements are currently in the table.

```text
              items in table
load factor = ---------------
              size of table
```

## Open Addressing main idea
When we want to insert a key-value pair (k,v) into a hash table, we hash the key and obtain the original position where this key-value pair belongs, i.e. H(k).

If the position our key hashed to is occupied, we try another position in the hash table by `offsetting the current position subject to a probing sequence P(x)`. We keep doing this until an unoccupied slot is found.

## Probing method
### Linear Probing
```text
P(x) = ax + b, where a,b constants
```
### Quadratic Probing
```text
P(x) = ax^2 + bx + c, where a,b,c constants
```
### Double Hashing
```text
P(k,x) = x*H(k), where H(k) is a secondary hash function  
```
