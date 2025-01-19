**https://leetcode.com/problems/one-edit-distance/submissions/1513495944/**

## правильное решени
```python
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        s1, s2 = s, t
        s1Len, s2Len = len(s1), len(s2)

        # If the length difference is greater than 1, it's not one edit distance
        if abs(s1Len - s2Len) > 1:
            return False

        edited = False
        s1Pointer, s2Pointer = 0, 0

        while s1Pointer < s1Len and s2Pointer < s2Len:
            if s1[s1Pointer] != s2[s2Pointer]:
                if edited:
                    return False  # More than one edit
                edited = True
                # Handle the three possible edit cases
                if s1Len > s2Len:  # Remove from s1
                    s1Pointer += 1
                elif s1Len < s2Len:  # Add to s1
                    s2Pointer += 1
                else:  # Replace
                    s1Pointer += 1
                    s2Pointer += 1
            else:
                s1Pointer += 1
                s2Pointer += 1

        # After the loop, consider the case where one string has an extra character
        if not edited:
            return abs(s1Len - s2Len) == 1

        return True
```


```python
# algoexpert
def oneEdit(stringOne, stringTwo):
    editsPerformed, allowedEdits = False, 1
    stringOneLenght, stringTwoLenght = len(stringOne), len(stringTwo)
    
    # edge case if lens diff is grater 1, 
    # means we can not achieve same strs after any 1 edit
    if abs(len(stringOne) - len(stringTwo)) > allowedEdits:
        return False
    
    pointerOne, pointerTwo = 0, 0
    while pointerOne < stringOneLenght and pointerTwo < stringTwoLenght:
        # case when we need to perform one of edit actions
        if stringOne[pointerOne] != stringTwo[pointerTwo]:
            # firstly check if we have used edit op already
            if editsPerformed:
                return False
            # if here, we do have 1 edit available
            else:
                # lens are different
                # perform "remove" op, remove from first str
                # move pointer of string, from where we remove char (1st str)
                if stringOneLenght > stringTwoLenght:
                    pointerOne += 1
                # lens are different
                # perform "add" op, add to first str
                # move pointer of opposite string, where we added char (2nd str)
                elif stringOneLenght < stringTwoLenght:
                    pointerTwo += 1
                # perform "replace" op, because lens are equal
                # move both pointers
                else:
                    pointerOne += 1
                    pointerTwo += 1
                # mark editPerformed as True, cause we perform edit op now
                editsPerformed = True
        # case when chars are equal, just move forward
        else:
            pointerOne += 1
            pointerTwo += 1
    return True
```


## оценку по времени и памяти
- Time: O(n+m), m and n lens of strs
- Space: O(1)

## идея
```text
we have 3 edit operations and we need to use only one of them
    - remove
    - add
    - replace

consider:
    - we might use ONLY 1 edit
    - replace to be used when len(s1) == len(s2) -> move both s1 and s2 pointers
    - delete to be used when len(s1) > len(s2) -> move s1 pointer
    - add to be used when len(s1) < len(s2) -> move ss pointer

idea
    (same lens)
    (1) replace
    if strings are same size - we need replace operation
    traverse chars, compare them and count replace operations
    if at any point replace ops were > 1 --> False

    (different lens)
    (2 | 3) remove | add
    (remove)
    traverse chars, compare them if different, remove char from longer string
    + count remove operations + move only pointer for str from which "removed"
    if at any point remove ops were > 1 --> False
    
    (add)
    traverse chars, compare them if different, add char to shorted string
    + count add operations + move only pointer for str to which "added"
    if at any point add ops were > 1 --> False

Time  O(n+m), n and m lens of 2 strings
Space O(1)
```
