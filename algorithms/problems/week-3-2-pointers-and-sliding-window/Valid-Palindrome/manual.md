**https://leetcode.com/problems/valid-palindrome/description/**

## правильное решени
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        cleansed = ''.join(char.lower() for char in s if char.isalnum())
        left, right = 0, len(cleansed)-1

        while left <= right:
            if cleansed[left] != cleansed[right]:
                return False
            left += 1
            right -= 1
        return True
```

## оценку по времени и памяти
- Time: O(n)    where n is sum of O(n) <-- stands for cleansing + O(n) <-- stands for traversing a string
- Space: O(m)   where m is the chars number after cleasning

## путь по которому вы пришли к решению
- cast input to valid format
- 2 pointers, from start and end, if loop passed (chars[l] == chars[r]) -- True, else Fasle

## идея
- cast input to valid format
- 2 pointers, from start and end, if loop passed (chars[l] == chars[r]) -- True, else Fasle
