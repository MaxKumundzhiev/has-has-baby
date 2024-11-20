**https://leetcode.com/problems/intersection-of-two-arrays/description/**

## правильное решени
```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        p1, p2 = 0, 0
        b1, b2 = len(nums1)-1, len(nums2)-1

        nums1.sort()
        nums2.sort()
        
        while (p1 <= b1) and (p2 <= b2):
            val1, val2 = nums1[p1], nums2[p2]
            if val1 == val2 and val1 not in ans:
                ans.add(val1)
                p1 += 1
                p2 += 1
            else:
                if val1 < val2:
                    p1 += 1
                else:
                    p2 += 1
        return list(ans)
```

## оценку по времени и памяти
- Time: O(n*log(n))
- Space: O(1) ~O(n)

## идея
```text
sort both arrays in ascdending order
    2 pointers, pointer for each array
    traverse while one of the pointers didnt exceed boundaries and compare values at pointers
        - if values are equal and such value is not in set
            add value to set
            move both
        - else
            find at which pointer the lowest value and move it's idx
```
