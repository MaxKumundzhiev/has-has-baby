**https://leetcode.com/problems/valid-anagram/description/**

## правильное решени
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        valid_to_check = True if len(s) == len(t) else False
        if not valid_to_check:
            return False
        
        s_map, t_map = dict(), dict()
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        
        for char, cnt in s_map.items():
            if char not in t_map:
                return False
            if cnt != t_map[char]:
                return False
        return True
```

## оценку по времени и памяти
- Time  O(n+m)
- Space O(26) = O(1)

## путь по которому вы пришли к решению

## идея
```json
2 strings are anagramms if amount of frequency of digits are equal and thier length are equal as well 

compose 2 frequency hashmaps per each word
traverse any of words hashmaps and check if char is presented in another hashmap and frequencies are equal

---------------------------------------------------

there is another approach
- compose frequency hashmap for any word first
- start traversing second
    - check if char is presented in hashmap
    - check if value > 0
        - if no, return False
    - decrese value
- if traversed and not returned, return True
```


