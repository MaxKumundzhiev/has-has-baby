**https://leetcode.com/problems/container-with-most-water/description/**

## правильное решени
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVolume = 0
        l, r = 0, len(height)-1
        while l < r:
            leftHeight, rightHeight = height[l], height[r]
            currVolume = min(leftHeight, rightHeight) * (r - l)
            maxVolume = max(maxVolume, currVolume)
            if leftHeight < rightHeight:
                l += 1
            else:
                r -= 1
        return maxVolume
```

## оценку по времени и памяти
- Time: O(n)
- Space: O(1)

## идея
most important to get formula for counting volume (area). Other than that, just compare all potential containers bounded from left and right heights.

```text
2 pointers, from start and end
define maxVolume = 0
on each iteration:
    count currVolume: min(height[l], height[r]) * (r-l)
    update maxVolume = max(maxVolume, currVolume)
    move pointer with the lowest value
```    