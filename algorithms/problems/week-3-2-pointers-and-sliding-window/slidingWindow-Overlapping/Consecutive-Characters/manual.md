**https://leetcode.com/problems/consecutive-characters/**

## правильное решени
```python
class Solution:
    def maxPower(self, s: str) -> int:
        mostLeftIdx = 0
        maxLength = 0
        hashmap = {}
        
        for currIdx in range(len(s)):
            # add every particular char within iteration into hashmap
            hashmap[s[currIdx]] = hashmap.get(s[currIdx], 0) + 1

            # check if window is in excpected condition (only distinct chars)
            # if so, shrink window to meet excpected condition
            while len(hashmap) > 1:
                hashmap[s[mostLeftIdx]] -= 1
                if hashmap[s[mostLeftIdx]] == 0:
                    del hashmap[s[mostLeftIdx]]
                mostLeftIdx += 1
            
            # measure potential window length
            maxLength = max(maxLength, currIdx-mostLeftIdx+1)
        return maxLength
```

## оценку по времени и памяти
- Time: O(s)
- Space: O(1)

## идея
```text
we gonna move currIdx to the end of the string
we gonna add char at currIdx in hashmap
we gonna measure len hashmap
    if len(hashmap) > 1:
        shrink window by decrementing | removing char from hashmap and moving mostLeftIdx
```