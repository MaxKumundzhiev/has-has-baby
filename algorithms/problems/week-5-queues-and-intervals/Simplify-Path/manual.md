**https://leetcode.com/problems/simplify-path/description/**

## правильное решени
```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories = path.split('/')
        for dir in directories:
            if dir == '.' or not dir:
                continue
            elif dir == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return '/' + '/'.join(stack)

```

## оценку по времени и памяти
- Time  O(n) + O(n) + O(1) + O(1) = O(n)
- Space O(n) + O(n)               = O(n)

## путь по которому вы пришли к решению
```
- str always start with /
- rules
    .   - curr dir
    ..  - parent dir (previous)
    /// - single slash
    ... - valid filename or dir

- canonical
    path must start with /
    dirs must be separated by /
    path should not end with /, unless its root dir
    path should not have any periods  

/home/user/Documents/../Pictures

- split on input string
[home, user, Documents, .., Pictures]

- construct stack based on rules
    - initiate stack ["/"]
    - traverse array
    - clean up word (in case if it has trailing or ending slashes)
    - if entity == word:
        stack.append(word)
    - # edge cases
    (1) if .  - continue
    (2) if .. - stack.pop()
    (3) if > .. - stack.append(> ..)
```

## идея
