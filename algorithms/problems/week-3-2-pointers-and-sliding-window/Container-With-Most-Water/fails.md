## 1 attempt
- Time Limit Exceeded - forgot manage left and right pointers
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
        return True
```