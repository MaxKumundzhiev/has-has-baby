**https://leetcode.com/problems/group-anagrams/description/**

## правильное решени
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for word in strs:
            key = ''.join(sorted(word.lower()))
            if key not in hash_map:
                hash_map[key] = [word]
            else:
                current = hash_map[key]
                current.append(word)
                hash_map[key] = current
        annagrams = []
        for annagram in hash_map.values():
            annagrams.append(annagram)
        return annagrams
```

## оценку по времени и памяти
- Время: O(n * k * log(k)), где n - количество строк, k - максимальная длина строки.
- Память: O(n * k)

## путь по которому вы пришли к решению
Самостоятельно

## идея
```
2 strings are anagramms - if thier amount of chars and lens are equal 

- introduce hash map
- traverse per word in strs
    - sort and lowercase a word
    - if word not in hash map
        - add word as a key and list[word] as value (unsorted word)
    else
        - update by key a value (add word (unsorted) to list)

- traverse a hash map and res from hash map to final result
```