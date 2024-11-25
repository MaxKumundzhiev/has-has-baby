**https://leetcode.com/problems/longest-repeating-character-replacement/description/**

## правильное решени
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        frequency_map = {}
        max_frequency = 0
        longest_substring_length = 0
        
        for end in range(len(s)):
            frequency_map[s[end]] = frequency_map.get(s[end], 0) + 1

            # the maximum frequency we have seen in any window yet
            max_frequency = max(max_frequency, frequency_map[s[end]])

            # move the start pointer towards right if the current
            # window is invalid
            is_valid = (end + 1 - start - max_frequency <= k)
            if not is_valid:
                frequency_map[s[start]] -= 1
                start += 1

            # the window is valid at this point, store length
            # size of the window never decreases
            longest_substring_length = end + 1 - start

        return longest_substring_length
```

## оценку по времени и памяти
- Time: O(s)
- Space: O(1)

## идея
```text
find the longest substring with consequitive chars (distinct) and potential swaps at most k
sliding window, non fixed lenght, answers might overlap

hashmap = {s[0]:1}
on each iteration
    while left < len(nums):
        while right+1 < len(nums) and s[r+1] in hashmap or k > 0:
            if s[r+1] in hashmap:
                hashmap[s[r+1]] += 1
            ...
            right += 1
```