**https://leetcode.com/problems/car-pooling/description/**

## правильное решени
```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        pickUps = sorted([(trip[0],trip[1]) for trip in trips], key = lambda x: x[1])
        dropOffs = sorted([(trip[0],trip[2]) for trip in trips], key = lambda x: x[1])
        
        pick, drop = 0, 0
        while pick < len(pickUps):
            if pickUps[pick][1] < dropOffs[drop][1]:
                capacity -= pickUps[pick][0]
            else:
                capacity += dropOffs[drop][0]
                drop += 1
                continue
            pick += 1

            if capacity < 0:
                return False
            
        return capacity >= 0
```
OR
```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        startEventType, endEventType = +1, -1
        for idx in range(len(trips)):
            passengers, start, end = trips[idx]
            events.append([start, passengers, startEventType])
            events.append([end, passengers, endEventType])
        events.sort()

        currentCapacity = 0
        for event in events:
            _, passengers, eventType = event
            if eventType == startEventType:
                currentCapacity += passengers
            else:
                currentCapacity -= passengers
            if currentCapacity > capacity:
                return False
        return True
```

## оценку по времени и памяти
- Time sort(O(n*log(n))) + array(O(n)) + traverse(O(n)) = O(n*log(n))
- Space sort(O(n)) + array(O(n))                        = O(n)

## путь по которому вы пришли к решению
```json
capacity = X
trips = [[2,1,5], [3,3,7]]


------
1    5
  ------
  3    7

1. sort *events by 2nd value (start event)
2. construct events array, with convention: [coordinate, passangers]
3. initiate currentCapacity = 0
4. traverse all events
    - update currentCapacity
    - if currentCapacity > capacity:
        return False
5. return True

events = [
    [1, +2], [3, +3], [5, -2], [7, -3]
]
```

## идея
