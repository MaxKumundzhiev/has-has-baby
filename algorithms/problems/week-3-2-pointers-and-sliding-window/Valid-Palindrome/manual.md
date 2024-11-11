**https://leetcode.com/problems/valid-palindrome/description/**

## правильное решени
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        casted = ''.join(char.lower() for char in s if char.isalnum())
        
        l, r = 0, len(casted)-1
        while l <= r:
            leftChar, rightChar = casted[l], casted[r]
            if leftChar != rightChar:
                return False
            l += 1
            r -= 1
        return True
```

## оценку по времени и памяти
- Time: O(n)    where n is sum of O(n) <-- stands for cleansing + O(n) <-- stands for traversing a string
- Space: O(m)   where m is the chars number after cleasning

## идея
- cast input to valid format
- 2 pointers, from start and end, if loop passed (chars[l] == chars[r]) -- True, else Fasle
