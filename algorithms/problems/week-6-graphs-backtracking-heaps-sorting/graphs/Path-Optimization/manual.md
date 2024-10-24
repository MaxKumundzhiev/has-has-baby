**private**

## условие
Дана строка s, содержащая сиваолы
- U - вверх
- D - вниз
- L - влево
- R - вправо

Нужно избавиться от всех циклов в маршруте и сделать его оптимальным. Нужно именно сократить маршрут, а не сделать новый. Под петлей в задаче подразумается части маршрута, котороые возвразают нас в точку, в котрой мы были несколько шагов назад и убрав которые место прибытия не изменится.

## правильное решени
```python
from typing import *

def optimize_path(path: List[str]) -> List[str]:
    directions = {
        "R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)
    }
    opposite_directions = {
        "R": (-1, 0), "L": (1, 0), "U": (0, -1), "D": (0, 1)
    }
    x, y = 0, 0
    used = {(0,0)}
    result = []
    for idx in range(len(path)):
        step = path[idx]
        next_x, next_y = x + directions[step][0], y + directions[step][1]
        if (next_x, next_y) not in used:
            used.add(tuple([next_x, next_y]))
            result.append(step)
            x, y = next_x, next_y
        while [next_x, next_y] != [x, y]:
            _ = result_pop()
            used.remove(tuple([x, y]))
            x, y = x + opposite_directions[step][0], y + opposite_directions[step][1]
    return result
```

## оценку по времени и памяти
- Time: O()
- Space: O()

## путь по которому вы пришли к решению
разбор

## идея
Давайте когда мы будем возвразаться в ту точку где мы уже были, будем стирать все предыдущие