**https://leetcode.com/problems/meeting-rooms-ii/description/?envType=problem-list-v2&envId=52dlem1s**

## правильное решени
```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for interval in intervals:
            start, end = interval[0], interval[1]
            events.append([start, +1])
            events.append([end, -1])
        
        events.sort()
        counter, maxCounter = 0, 0
        for event in events:
            counter += event[1]
            maxCounter = max(maxCounter, counter)
        return maxCounter
```

## оценку по времени и памяти
- Time O(n*log(n))
- Space O(n)

## идея
```text
Idea:
    use method of points (when u need to count something against intervals)
    minimum number of conference rooms == find max number of intersections
```