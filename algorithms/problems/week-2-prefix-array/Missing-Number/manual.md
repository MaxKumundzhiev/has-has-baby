**https://leetcode.com/problems/missing-number/description/**

## правильное решени
```python
# optimized solution Time O(n) Space O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length_inclusivly = len(nums)+1

        totalSum = 0
        for number in range(length_inclusivly):
            totalSum += number
        
        currentSum = 0
        for number in nums:
            currentSum += number
        
        return totalSum - currentSum
```

```python
# naive solution Time O(n) Space O(n)
"""
- range from [0, n], where  1 <= n <= 10.000
- all numbers are unique
- by condition only 1 number is missing

EXAMPLEs:
    [1, 3, 4] --> 2
    [3,0,1]   --> 2

- get the len of numbers: 3
- preallocate the hash table for those numbers: {number:did_we_met}
- traverse the numbers and fulful the hash table
- traverse the hash table and look up key with value False

Time  O(n) + O(n) = O(2n) = O(n)
Space O(n)
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        inclusive_length = len(nums)+1
        
        hash_table = {}
        for number in range(inclusive_length):
            hash_table[number] = False
        
        for number in nums:
            hash_table[number] = True
        
        for value, exists in hash_table.items():
            if exists is False:
                return value
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(1)

## путь по которому вы пришли к решению
Сначала я решил не оптимально по памяти, а именно подсчитав ожидаемый рендж, я предзаполнил хэш таблицу по структуре {value:exists}, где изначально у всех значений exists был False. Дальше я прошелся по инпуту и проверил, какие значения мы встретил и пометил их как True. И последним действием, я обошел заполненную хэш таблицу, в поиске того единственного елемента, у которого значение было False. 

После, увидев, что можно оптимальнее, я спразу пришел к идее, что нужно посчитать общую сумма, и потом использовать ее для подсчета пропузенного элменета. Сначала я немного усложнил, добавив currentSum и remainingSum и пытался их менеджить одновременно. А потом понял, что можно обойтись всего лишь currentSum и после вычесть из ранее посчитанной totalSum.


## идея
Идея оптимального решения в том, чтобы рабоать с суммой ренджа (взятого на основе длины инпута).
Когда мы знаем общую сумму и сумму интервала от инпута, мы можем просто вычесть одного их другого - разница это и будет пропущенный элеменет.

