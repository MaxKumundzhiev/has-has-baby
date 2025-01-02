**https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/**

## правильное решение
```python
class Solution:
    keyboard: dict = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }

    def backtracking(self, idx:int, digits:str, currentCombination:str, allCombinations:list[str]):
        # base case
        # when all the combination is composed
        if idx == len(digits):
            concated = "".join(currentCombination)
            allCombinations.append(concated)
            return
        
        digit = digits[idx]
        for letter in self.keyboard[digit]:
            # add new letter to current combination
            currentCombination.append(letter)
            # traverse all options for current letter
            self.backtracking(
                idx=idx+1, 
                digits=digits, 
                currentCombination=currentCombination, 
                allCombinations=allCombinations
            )
            # pop the letter, cause already traversed all options for it
            currentCombination.pop()


    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        if len(digits) == 0: return combinations

        self.backtracking(
            idx=0,
            digits=digits,
            currentCombination=[],
            allCombinations=combinations
        )
        return combinations
```

## оценку по времени и памяти
- Time: O()
- Space: O()

## идея