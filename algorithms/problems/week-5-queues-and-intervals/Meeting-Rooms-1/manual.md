**https://leetcode.com/problems/meeting-rooms/description/?envType=problem-list-v2&envId=52dlem1s**

## правильное решени
```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for currMeetIdx in range(len(intervals)-1):
            currMeet, nextMeet = intervals[currMeetIdx], intervals[currMeetIdx+1]
            intersect = max(currMeet[0], nextMeet[0]) < min(currMeet[1], nextMeet[1])
            if intersect:
                return False
        return True
```

## оценку по времени и памяти
- Time O(n*logn(n))
- Space O(1)

## идея
The idea here is to sort the meetings by starting time. Then, go through the meetings one by one and make sure `that each meeting ends before the next one starts` (there is no intersection).