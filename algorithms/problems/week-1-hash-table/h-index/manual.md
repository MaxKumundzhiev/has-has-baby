**https://leetcode.com/problems/h-index/description/**

## правильное решени
```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n + 1)

        # Считаем сколько раз встречается каждая цитата
        for el in citations:
            count[min(el, n)] += 1

        papers_count = 0
        # Проверяем h-индекс начиная с максимального
        for h_index in range(n, -1, -1):
            papers_count += count[h_index]
            if papers_count >= h_index:
                return h_index
        return 0
```

## оценку по времени и памяти
- Time  O(n)
- Space O(n)

## путь по которому вы пришли к решению
Разбор

## идея
```json
if h-index equals to X
    Q: is there X numbers (idxs) whos' value >= X
       find max number of idx, whose value > amount idxs 
    N:
        h-index can not be grater of amount of papers (len of citations)

example: [3,0,6,1,5]
          0 1 2 3 4

1. создадим и заполним массив count 
(подсчитаем сколько раз каждое число встретилось, только через массив)
(индекс в массиве означает число, а значение означает количество раз сколько встретилось это число)
    -----------------------------------
    count = [0, 0, 0, 0, 0]
    e.g.: idx=1, thus count[idx] - 0 статей, которые цитировали 1 раз
    e.g.: idx=5, thus count[idx] - 0 статей, которые цитировали 5 раз
    -----------------------------------
    e.g.: value=6 at idx=2
    count[min(value, len(example)-1)] += 1 # because h-index can not be grater of amount of papers
2. заводим счетчик количества цитат и начинаем итерироваться с максимальноно h-index в обратную сторону, который равен длине цитат (кол-во бумаг). на каждой итерации проверяем если количество циатат >= h-index
    -----------------------------------
    count   = [1, 1, 0, 1, 2]
    h-index =  0  1  2  3  4
    -----------------------------------
```