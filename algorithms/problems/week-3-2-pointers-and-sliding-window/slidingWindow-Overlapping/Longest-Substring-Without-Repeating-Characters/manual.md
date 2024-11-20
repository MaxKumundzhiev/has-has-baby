**https://leetcode.com/problems/longest-substring-without-repeating-characters/description/**

## правильное решени
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        interval = set()
        maxLength = 0
        l, r = 0, -1
        
        while l < len(s):
            # constrcuting interval (non-repeatable chars)
            while r+1 < len(s) and s[r+1] not in interval:
                interval.add(s[r+1])
                r += 1
            # constructed interval (non-repeatable chars)
            # measure len and compare with previous len
            maxLength = max(maxLength, r-l+1)
            # remove char on left piosition from interval
            # and move left pointer on the next position
            interval.remove(s[l])
            l += 1
        return maxLength
```

## оценку по времени и памяти
- Time: O(s)
- Space: O(k), where k amount of unique elements

## идея
```text
      |
 abcabcbb
        |

r = {a, c, b}
idea
    sliding window, ovelapping intervals (answers)
    l, r pointers, r will be -1, left 0, at the beginning --> to keep processing same for all the chars
    interval = set()
    look up at r+1 position char into interval 
    if such char does not exist in interval
        add char
        move r to r+1
    else
        measure and record max len of interval
        remove char at position l from interval
        move l positionm to l + 1


Time  O(s)
Space O(max(len(consequtiveNonRepeatableChars))) ~ O(26) ~ O(1)
```