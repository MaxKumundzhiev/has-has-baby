**https://leetcode.com/problems/find-all-anagrams-in-a-string/**

## правильное решени
```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Finds all anagram indices of `p` in `s`.

        Args:
            s: The source string.
            p: The target string.

        Returns:
            A list of indices where anagrams of `p` start in `s`.
        """

        if len(p) > len(s):
            return []

        # Create character frequency maps for the initial window
        p_count, s_count = {}, {}
        for i in range(len(p)):
            p_count[p[i]] = p_count.get(p[i], 0) + 1
            s_count[s[i]] = s_count.get(s[i], 0) + 1

        # Initialize pointers and result list
        left, right, result = 0, len(p) - 1, []

        while right < len(s):
            # Check if current window is an anagram
            if p_count == s_count:
                result.append(left)

            # Slide the window:
            # - Remove the leftmost character from the window
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                s_count.pop(s[left])
            left += 1

            # Add the rightmost character to the window
            right += 1
            if right < len(s):  # Important: Check if right is within bounds
                s_count[s[right]] = s_count.get(s[right], 0) + 1

        return result
```

## оценку по времени и памяти
- Time   O(s)
- Space  O(1), with 26 eng alphabet max

## путь по которому вы пришли к решению
Разбор

## идея
- compose target count hashmap for p
- traverse within fixed sliding window over s string
    - compose source count hashmap for window word
    - compare source and target count hashmaps
    - if equal (anagrams), add starting position to result
    - else
        move right pointer to +1 position
        add right pointer value to source hashmap 
        remove left pointer value from source hashmap
        move left pointer to +1 position