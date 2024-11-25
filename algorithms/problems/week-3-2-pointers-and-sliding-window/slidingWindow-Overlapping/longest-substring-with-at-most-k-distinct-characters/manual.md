****

## правильное решени
```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        maxLength = 0
        hashmap = {}

        for right in range(len(s)):
            # on each iter add char into hashmap (window)
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            # make sure hashmap (window) satisfied condition (distinct chars at most k)
            while len(hashmap) > k:
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    del hashmap[s[left]]
                left += 1
            # window is valid -- measure it's length
            maxLength = max(maxLength, right-left+1)
        return maxLength
```

## оценку по времени и памяти
- Time: O(s)
- Space: O(1)

## идея
```text
sliding window, not fixed length, answers overlap
2 pointers, left, right + hashmap
on each iteration add char into hashmap
# if window not in condition
while len hashmap > k:
    shrink window by removing charts at left idx from hashmap
measure maxLenght = max(maxLenght, right-left+1)
```