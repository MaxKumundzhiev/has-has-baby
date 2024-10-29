**https://leetcode.com/problems/top-k-frequent-elements/**

## правильное решени
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for number in nums:
            counter[number] = counter.get(number, 0) + 1
        
        potential_unique_numbers = len(nums)+1
        frequencies = [[] for _ in range(potential_unique_numbers)]
        for number, frequency in counter.items():
            frequencies[frequency].append(number)
        
        top_k = []
        for frequency in reversed(frequencies):
            for number in frequency:
                if k <= 0:
                    return top_k
                top_k.append(number)
                k -= 1
        return top_k
```

## оценку по времени и памяти
- Time  O()
- Space O()

## путь по которому вы пришли к решению
Разбор

## идея
1. compose value:frequency hashmap
2. count lenght (+1) of values in original array (that would be amount of arrays in frequency array)
3. compose 2d array of frequency(idx):values(array)(frequency key contains all the elements which occurred "frequency" times)
4. traverse from the end of array, until k != 0 and populate result array

```
# допустим у нас получиллся такой frequencCounter:
{
    2:1,
    5:1,
    4:3
}

# здесь индекс == сколько раз такое число встретилось
# допустим у нас получиллся такой frequencyList:
        # 0: []
        # 1: [2, 5]  # 2 и 5 встретились 1 раз
        # 2: []
        # 3: [4]     # 4 встретилось 3 раза
        # 4: []
        # 5: []
        # при k = 1 нам нужно вернуть 4
        # для этого проходимся с конца и ищем первые k элементов
```