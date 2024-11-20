**https://leetcode.com/problems/backspace-string-compare/**

## правильное решени
```python
class Solution:
    def findNextNonSkip(self, s: str, i: int) -> int:
        skipCount = 0
        while i >= 0 and (skipCount > 0 or s[i] == '#'):
            if s[i] == '#':
                skipCount += 1
                i -= 1
                continue
            skipCount -= 1
            i -= 1
        return i

    def backspaceCompare(self, s: str, t: str) -> bool:
        p1, p2 = len(s), len(t)
        while p1 > 0 and p2 > 0:
            p1 = self.findNextNonSkip(s, p1 - 1)
            p2 = self.findNextNonSkip(t, p2 - 1)
            if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
                return False
        return self.findNextNonSkip(s, p1 - 1) == self.findNextNonSkip(t, p2 - 1)
```

## оценку по времени и памяти
- Time: O(n + m)
- Space: O(1)

## идея
```text
O(n)
O(n)
naive:
    traverse both strings and "clean them up" O(n)
    traverse resulting strings and compare them O(n)

O(n)
O(1)
optimized:
    traverse from the end
    use additional method and skipCounter to skip backspace symbols
```
