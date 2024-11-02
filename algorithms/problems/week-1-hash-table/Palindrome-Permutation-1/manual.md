**https://leetcode.com/problems/palindrome-permutation/description/**

## правильное решени
```python
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = [0] * 26
        for char in s:
            idx = ord(char) - ord('a')
            counter[idx] += 1
        odds = 0
        for cnt in counter:
            if odds > 1:
                return False
            if cnt % 2 != 0:
                odds += 1
        return True
```

## оценку по времени и памяти
- Time  O(n)
- Space O(1)

## идея
- проверить алфавит
- сделать count sort на массиве (посчитать количество букв и сколько они встречаются)
- воспользоваться свойством палиндрома (если нечетных букв <= 1 - палиндром, иначе нет)(проийтись по counter и проверить сколько нечетных букв)