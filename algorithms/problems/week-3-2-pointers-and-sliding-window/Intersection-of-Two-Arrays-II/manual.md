**https://leetcode.com/problems/intersection-of-two-arrays-ii/description/**

## правильное решени
```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        p1, p2 = 0, 0
        answ = []
        while (p1 < len(nums1)) and (p2 < len(nums2)):
            val1, val2 = nums1[p1], nums2[p2]
            if val1 > val2:
                p2 += 1
            elif val1 < val2:
                p1 += 1
            else:
                answ.append(val1)
                p1 += 1
                p2 += 1
        return answ
```

## оценку по времени и памяти
- Time: O(n*logn)
- Space: O(n)

## идея
```text
- sort arrays in asd order O(nlogn)
- 2 pointers, pointer on each array
- traverse until elements in both arrays are present
    - if val1 == val2: 
        append
        move both pointers
    - elif val1 > val2:
        move p2
    - else:
        move p1
```
