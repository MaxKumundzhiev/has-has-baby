**https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/**

## правильное решени
```python
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_in_a = dict()
        seen_in_b = dict()
        result = []

        for a, b in zip(A, B):
            in_common, to_add_up = 0, 0
            if a in seen_in_b:
                in_common += seen_in_b[a]
            if b in seen_in_a:
                in_common += seen_in_a[b]
            if a == b:
                in_common += 1

            seen_in_a[a] = seen_in_a.get(a, 0) + 1
            seen_in_b[b] = seen_in_b.get(b, 0) + 1
            if bool(result):
                to_add_up = result[-1]
            result.append(in_common + to_add_up)
        return result
```

## оценку по времени и памяти
- Time  O(n)
- Space O(n+m), where n and m is amount of unique numbers in array A and array B

## путь по которому вы пришли к решению
Самостоятельно

## идея
- сколько общих элементов на том или ином префиксе
- завести по hashmap на каждый из массивов, где будем хранить число:частотность
- на каждой итерации смотреть сколько раз встретили число из A в B и наоборот
- также проверять если числа равны
- и не забыть добавить кол-во общих элементов с прошлой итерации

```
a       --> 2 1 3 4 5
b       --> 3 1 2 5 4
            |
сколько здесь общих элементов 

prf     --> 0 1 3 3 5
           
```
