**private**

## условие
Дана строка, содержащая символы
- U - вверх
- D - вниз
- L - влево
- R - вправо

Нужно избавиться от всех циклов в маршруте и сделать его оптимальным. Нужно именно сократить маршрут, а не сделать новый. Под петлей в задаче подразумается части маршрута, котороые возвразают нас в точку, в котрой мы были несколько шагов назад и убрав которые место прибытия не изменится.

```text
ввод: RDLUR
вывод: R

обьяснение: потому что делаем петлю RDLU
```

## правильное решени
```python
def optimised_path(steps: str) -> str:
    # mapping for steps when havent visited yet 
    mapping = {
        "R": (0,1),
        "L": (0,-1),
        "U": (-1,0),
        "D": (1,0),
    }
    
    # mapping for steps when have visited already
    # and need to backfill steps
    opposite_mapping = {
        "R": (0,-1),
        "L": (0,1),
        "U": (1,0),
        "D": (-1,0),
    }

    # define current coordinate to kick off traversal
    cur = (0,0)

    # kick off traversal
    visited, path = set(cur), list()
    for step in steps:
        # get the direction to move from mapping
        direction = mapping.get(step)
        # compose next step coordinate
        nxt = (cur[0]+direction[0], cur[1]+direction[1])

        # did not visit such coordinate yet
        # compose a step -> add to visited; path and update coordinates (cur)
        if nxt not in visited:
            visited.add(current_coordinate)
            path.append(step)
            cur = nxt
        
        # if already visited such coordinate, thus cycle detected, 
        # thus need to clean up both visited and path
        while cur != nxt:
            visited.remove(cur)
            step = path.pop()
            opposite_direction = opposite_mapping.get(step)
            nxt = (cur[0]+opposite_direction[0], cur[1]+opposite_direction[1])
    return result
```

## оценку по времени и памяти
- Time: O(n) - нужно обойти весь пусть
- Space: O(n) - нам понадобятся дополнительные структуры - в худшем случае нам в сете понадобятся все шаги

## идея
Давайте представим, что мы двигаемся по матрице. Также Давайте определим каждый шаг, как точку, в том смысле, что R - это сдвиг на (0,+1) и т.д. Также давайте заведем сет visited и результирующий массив path, куда будем добавлять каждый шаг (точку), но, до тех пор, пока не встретим шаг (точку) в сете visited, которая уже была. В случае, если мы встретили такую точку - запустим while цикл, который будет убирать точки из сета и результирующего массива.

Дополнительно, нужно: 
- обязательно ввести current (0,0) координату - откуда мы стартуем и добавить ее в visited
- для удобства рассчетов - ввести mapping и opposite mapping хэш таблицы
    - mapping будем использовать для рассчета след координаты, когда двигаемся вперед 
    - opposite mapping будем использовать для рассчета след координаты, когда двигаемся назад (чистим наш путь)