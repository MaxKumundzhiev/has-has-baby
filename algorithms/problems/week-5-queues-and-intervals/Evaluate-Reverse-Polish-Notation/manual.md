**https://leetcode.com/problems/evaluate-reverse-polish-notation/description/**

## правильное решени
```python
"""
traverse tokens
    if token not an operand, push a token to stack
    else
        if on len(stack) > 1:
            twice pop from stack in correct order tokens
        else
            once pop from stack
        compute and save into currentResult

"2","1","+","3","*"
3
res = 2 + 1 = 3 * 3 = 9

Time O(N) + O(1) + O(1) = O(N) 
Space O(M), where M amount if numbers in input
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                last = stack.pop()
                first = stack.pop()
                if token == "+":
                    stack.append(first + last)
                if token == "-":
                    stack.append(first - last)
                if token == "/":
                    stack.append(int(first / last))
                if token == "*":
                    stack.append(first * last)
        return stack[-1]
```

## оценку по времени и памяти
- Time: O(N)
- Space: O(M)

## путь по которому вы пришли к решению
Сразу придумал концепт про добавление элементов на стек до тех пор, пока не втретим операнд. Однако не сразу понял, что нужно класть результат на стек обратно. По моей версии нужно было считать сколько элементов на стеке, и если > 1, то снимать 2 в правильном порядке, иначе 1. После просмотра разбора, поправил.

## идея
Завести стек и маппинг или хеш сет операндов. Итерируемся по токенам, пока токен это не операнд (число), кладем на стек. Как только встретили операнд, снимаем со стека два последних числа (в правильном порядке) и производим опрецию (текущий токен говорит что за операция). Получившийся результат кладем обратно на стек. После пройденного цикла, на стеке будет лишь один элемент, который обозначает резальтат выражения - его и возвращаем.