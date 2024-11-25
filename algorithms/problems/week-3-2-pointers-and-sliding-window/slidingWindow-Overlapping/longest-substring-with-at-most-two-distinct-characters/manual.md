**https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/**

## правильное решени
```python
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        current = {}
        maxLength = 0

        for right in range(len(s)):
            # update current hashmap with income char
            current[s[right]] = current.get(s[right], 0) + 1

            # shrink current window (hashmap) until satisfy condition 2 distinct symbols
            while len(current) > 2:
                current[s[left]] -= 1
                if current[s[left]] == 0:
                    del current[s[left]]
                left += 1
            
            # update window max length
            maxLength = max(maxLength, right-left+1)

        return maxLength

```

## оценку по времени и памяти
- Time: O(s)
- Space: O(1)

## идея
```text
sliding window, non fixed window lenght, overlapping windows
hashmap for storing count of elements

compose window until hashmap len will be == 2
measure window lenght
remove mostLeft and mostRight elements from hashmap
```