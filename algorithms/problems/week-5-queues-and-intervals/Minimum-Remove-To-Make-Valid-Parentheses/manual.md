**https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/**

## правильное решени
```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        answer, openings, closing = [], [], []
        mapping = {"(": ")"}

        for idx, char in enumerate(s):
            openings_is_empty = True if not bool(openings) else False
            # edge case: char is alphabetic symbol, continue traversing
            if char.isalpha():
                continue
            # edge case: char is "(" opening bracket
            elif char in mapping:
                openings.append(idx)
            # edge case: char is ")" closing bracket
            # and openings is not empty
            # pop the last index
            elif openings_is_empty is False:
                _ = openings.pop()
            # edge case: char is ")" closing bracket
            # and openings is empty
            # add idx to closing, for further "removal"
            else:
                closing.append(idx)
        
        idxs_to_remove = openings + closing
        for idx, char in enumerate(s):
            if idx in idxs_to_remove:
                continue
            else:
                answer.append(char)
        return ''.join(answer)
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(n)

## путь по которому вы пришли к решению
Посмотрел разбор

## идея
- Идея с балансом открывающихся / закрывающихся скобок
- Идея про стек (очередь) + пометкой безпарных скобок*
```bash
создаем стек
начинаем итерироваться по строке
если символ не "()", идем дальше
если сивол "(" тогда мы кладем в стек индекс этой скобки
если символ ")" и стек не пустой, удаляем индекс
если символ ")" и стек пустой, помечаем этот элменет #

openings = []
closing = []
answer = []
```