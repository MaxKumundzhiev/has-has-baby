**https://leetcode.com/problems/squares-of-a-sorted-array/description/**

## правильное решени
```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans, power = [], 2
        l, r = 0, len(nums)-1
        while l <= r:
            leftVal, rightVal = pow(nums[l], power), pow(nums[r], power)
            # look up for the greatets
            if leftVal > rightVal:
                ans.append(leftVal)
                l += 1
            else:
                ans.append(rightVal)
                r -= 1
        ans.reverse()
        return ans
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(n)

## идея
Два указателя, на начало и конец по каждому, также заолоцировать результирующий массив и индекс вставки с конца. Далее итерируеся, пока указатели не пересекутся, где на каждой итерации сравниваем по модулю числа, вставляем большее число (его квадрат) в конец результирующего. Если вдруг числа равны по модулю, берем любое.

```text
optimized
    2 pointers, l and r pointer to the start and end of the array
    traverse until pointers overlap
    on each iteration, we gonna get sqrs of both numbers
    we gonna find whther the greatest sqr is on left or right pointer
    pick the greatest add it to the result and move the greatest pointer
```