**https://leetcode.com/problems/isomorphic-strings/description/**

## правильное решени
```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map, t_map = {}, {}
        for i in range(len(s)):
            if s[i] in s_map and s_map[s[i]] != t[i]:
                return False
            if t[i] in t_map and t_map[t[i]] != s[i]:
                return False
            s_map[s[i]] = t[i]
            t_map[t[i]] = s[i]
        return True
```

## оценку по времени и памяти
- Time  O(n)
- Space O(n)

## путь по которому вы пришли к решению

## идея
- завести по hashmap на каждую из строк
- начинаем итерироваться посимвольно по каждой строке одновременно
- проверяем каждый символ из строк отдельно
    - встречали ли уже иы этот символ (из s) - если да - проверим изоморфен ли он
    - встречали ли уже иы этот символ (из t) - если да - проверим изоморфен ли он
    - если один из них не изоморфер - выходим
    - иначе обновляем хэш мапы