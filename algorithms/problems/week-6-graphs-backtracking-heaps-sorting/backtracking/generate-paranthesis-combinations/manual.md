**https://leetcode.com/problems/generate-parentheses/description/**


## правильное решение
```python
class Solution:
    def generate(
        self, 
        expectedParenthesisAmount:int,
        balanceOpenedClosed:int, 
        currentParenthesis:list[str],
        allParenthesis:list[str]
    ):
        # base cases
        # (1)
        # according to balance balanceOpenedClosed 
        # balanceOpenedClosed < 0 - it means closed paranthes grater than open
        # balanceOpenedClosed > 0 - it means open paranthes grater than closed
        # balanceOpenedClosed > expectedParenthesisAmount - currentParenthesis - it means not enough paranthes to make sequence correct
        if balanceOpenedClosed < 0 or balanceOpenedClosed > (expectedParenthesisAmount - len(currentParenthesis)):
            return
        # (2)
        # sequence is composed, when amount of balanceOpenedClosed == 0 and len(currentParenthesis) == expectedParenthesisAmount
        if balanceOpenedClosed == 0 and len(currentParenthesis) == expectedParenthesisAmount:
            sequence = "".join(currentParenthesis)
            allParenthesis.append(sequence)
            return
        
        # generating backtracking logic
        # add parenthesis
        # recursivly generate for it all other states 
        # pop parenthesis (get back to previous state)
        openingState, closingState = ["(", balanceOpenedClosed+1], [")", balanceOpenedClosed-1]
        for parenthesis, updatedBalanceOpenedClosed in [openingState, closingState]:
            currentParenthesis.append(parenthesis)
            self.generate(
                expectedParenthesisAmount=expectedParenthesisAmount,
                balanceOpenedClosed=updatedBalanceOpenedClosed,
                currentParenthesis=currentParenthesis,
                allParenthesis=allParenthesis
            )
            currentParenthesis.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        allParenthesis, expectedParenthesisAmount, balanceOpenedClosed = [], n*2, 0
        self.generate(
            allParenthesis=allParenthesis,
            expectedParenthesisAmount=expectedParenthesisAmount,
            balanceOpenedClosed=balanceOpenedClosed,
            currentParenthesis=[]
        )
        return allParenthesis
```

## оценку по времени и памяти
можно взять числа каталана - оно показывает сколько возможных вариантов можно сшенерировать
- Time: O(C_n), где C_n - это числа каталана
- Space: O(C_n), где C_n - это числа каталана

## идея