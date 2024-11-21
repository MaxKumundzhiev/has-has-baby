**https://leetcode.com/problems/permutation-in-string/description/**

## правильное решени
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Create a hashmap to store character frequencies in s1
        source_count = {}
        for char in s1:
            source_count[char] = source_count.get(char, 0) + 1

        # Initialize a sliding window with the same size as s1
        window_count = {}
        for char in s2[:len(s1)]:
            window_count[char] = window_count.get(char, 0) + 1

        # Check if the initial window matches s1
        if window_count == source_count:
            return True

        # Slide the window
        for i in range(len(s1), len(s2)):
            # Add the new character to the right
            right_char = s2[i]
            window_count[right_char] = window_count.get(right_char, 0) + 1

            # Remove the leftmost character
            left_char = s2[i - len(s1)]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]

            # Check if the current window matches s1
            if window_count == source_count:
                return True

        return False
```

## оценку по времени и памяти
- Time: O()
- Space: O()

## идея
```text
1. sliding window, fixed size
2. permutation is the same as anagramma

thus, we might redefine our problem as: find an angram (which is s1) in s2, using sliding window of length s1 and 2 hashmaps (one for s1 and second for s2, but changable).
+ keep in mind, once formed a first window os size s1, we now need to move a window. to do so, we need to remove char at the most left position and add char at the mostright position.
```