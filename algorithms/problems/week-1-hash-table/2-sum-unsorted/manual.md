**https://leetcode.com/problems/two-sum/description/**

## правильное решени
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for idx, number in enumerate(nums):
            difference = target - number
            if difference in hashmap:
                return [hashmap[difference], idx]
            else:
               hashmap[number] = idx
```

## оценку по времени и памяти
- Time  O(n) + O(1) + O(1) = O(n)
- Space O(n)

## путь по которому вы пришли к решению
Самостоятельно

## идея
```json
hash map, to manage number we already met

- difference = target - current
- difference in hashmap
    - return [idx1, idx2]
- add number:idx at hashmap

# value: idx
{
    2: 0,
}
```