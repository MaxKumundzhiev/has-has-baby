**https://www.algoexpert.io/questions/run-length-encoding**

## правильное решени
```python
def runLengthEncoding(string):
    def encode(char: str, length: int) -> str:
        limit: int = 9
        # case if length <= 9
        if length <= limit:
            response = f"{length}{char}"
        # case if length > 9
        else:
            nines = length // limit  # get amount of nines in a length
            remains = length % limit
            response = [f"{limit}{char}" for _ in range(nines)]
            response.append(f"{remains}{char}")
        return response if isinstance(response, str) else "".join(response)
    
    result = []
    left, right = 0, 0
    while left < len(string):
        # accumalte consequitive window
        while right + 1 < len(string) and string[right] == string[right+1]:
            right += 1
        # window collapsed
        encoded = encode(char=string[right], length=(right-left)+1)
        result.append(encoded)
        # move left and right pointers
        left = right + 1
        right = right + 1
    
    return "".join(result)
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(n)

## идея
```text
We might split the problem on 2 smaller ones, whereas first one is to look up consecutive window of repeating chars and second one is to encode found window of repeating chars according to the compression conditions.

The first problem might be resolved with 2 pointers approach, both starting from the start and on each iteration checking if might traverse forward and whether previous char is equal to the next one.

The second problem might be resolved with mathematical intuition, precisely, looking up for the integer part (how many nines is there in a length of the window) and looking up whats the remaining part (whats the remaining part after "substracting" integer part from length of the window).

"""
integer = number // limit
remaining = number % limit
"""
```