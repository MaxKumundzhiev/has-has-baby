**https://leetcode.com/problems/number-of-islands/description/**

## правильное решение (DFS: recursive)
```python
class Solution:
    # land and water definition
    land, water = "1", "0"

    # down, left, up, right
    # coordinate: (rowIdx, columnIdx)
    steps = [
        (+1, 0),
        (0, -1),
        (-1, 0),
        (0, +1),
    ]

    def cell_is_in_boundaries(
        self, rowIdx: int, columnIdx: int, grid: list[list[str]]
    ) -> bool:
        rows, columns = len(grid), len(grid[0])
        return 0 <= rowIdx < rows and 0 <= columnIdx < columns

    def traverse(
        self, rowIdx: int, columnIdx: int, grid: list[list[str]], visited: list[list[bool]]
    ) -> None:
        # before proceeding further, check if the cell is valid
        if (
            not self.cell_is_in_boundaries(rowIdx, columnIdx, grid)
            or visited[rowIdx][columnIdx] is True
            or grid[rowIdx][columnIdx] == self.water
        ):
            return

        # mark the current cell as visited
        visited[rowIdx][columnIdx] = True

        # recursively visit all neighboring cells
        for step in self.steps:
            nextRow, nextColumn = rowIdx + step[0], columnIdx + step[1]
            self.traverse(nextRow, nextColumn, grid, visited)

    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        rows, columns = len(grid), len(grid[0])
        visited = [[False for _ in range(columns)] for _ in range(rows)]

        for rowIdx in range(rows):
            for columnIdx in range(columns):
                # to start traversal:
                # (1) cell must be land
                # (2) cell must not be visited
                if grid[rowIdx][columnIdx] == self.land and not visited[rowIdx][columnIdx]:
                    self.traverse(rowIdx, columnIdx, grid, visited)
                    islands += 1
        return islands
```

## оценку по времени и памяти
- Time: O(V + E)
- Space: O(V)

## идея
```text
идея
введя в задачу определения нулей (черные - вода) и единиц (белые - суша) - мы можем перефразировать задачу как: сколько покрасок нужно сделать, чтобы единиц (белые - суша) не осталось.

для того, чтобы запоминать, что вершину (клетку) мы посетили, введем массив такого же размера, как входной, назовем его visited и присвоим всем клеткам значения False (так как еще ничего не посетили) - а после посещения будем помечать ее как True.

и так, мы будем идти по нашей матрицы слева направо, сверху вниз, на каждой клетке мы будет проверять 2 условия: (1) клетка 1 (белая - суша) из входного массива И (2) клетка еще не посещена из массива visited - если условия удовлетворены - мы запускаем или dfs или bfs - иначе, переходим на следующую клетку. 

представим, мы будем пользоваться dfs, и будем двигаться вниз, влево, вверх, вправо - по часовой стрелке.

также когда запускаем обход: прежде, чем делать шаг обхода
 (помимо первичной проверки) - будем проверять, наша вершина (клетка) вообще пригодна или нет - то есть в диапазоне ли она   

 
заметки
- граф представлен в виде карты (матрицы) из 0 и 1
- есть 2 стандартных способа обхода графов - в ширину и в глубину
- можем ввести, что 0 - черные клетки, 1 - белые клетки
- когда 0 - черные клетки, 1 - белые клетки, мы можем запускать обход из белых клеток в нужные направления, крася из в черных (или делая 0-ли, 1-цами)
- если dfs итеративный - stack
- если bfs итеративный - queue
- диапозон:
0 <= rowIdx < rows and 0 <= columnIdx < columns
```

## правильное решение (DFS: iterative (stack))
```python
class Solution:
    # land and water definition
    land, water = "1", "0"

    # down, left, up, right
    # coordinate: (rowIdx, columnIdx)
    steps = [
        (+1, 0),
        (0, -1),
        (-1, 0),
        (0, +1),
    ]

    def cell_is_in_boundaries(
        self, rowIdx: int, columnIdx: int, grid: list[list[str]]
    ) -> bool:
        rows, columns = len(grid), len(grid[0])
        return 0 <= rowIdx < rows and 0 <= columnIdx < columns

    def traverse(
        self, rowIdx: int, columnIdx: int, grid: list[list[str]], visited: list[list[bool]]
    ) -> None:
        stack = deque([(rowIdx, columnIdx)])
        visited[rowIdx][columnIdx] = True

        while stack:
            rowIdx, columnIdx = stack.pop()
            for step in self.steps:
                nextRowIdx, nextColumnIdx = rowIdx + step[0], columnIdx + step[1]
                if (
                    not self.cell_is_in_boundaries(nextRowIdx, nextColumnIdx, grid)
                    or visited[nextRowIdx][nextColumnIdx]
                    or grid[nextRowIdx][nextColumnIdx] == self.water
                ):
                    continue
                stack.append((nextRowIdx, nextColumnIdx))
                visited[nextRowIdx][nextColumnIdx] = True

    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        rows, columns = len(grid), len(grid[0])
        visited = [[False for _ in range(columns)] for _ in range(rows)]

        for rowIdx in range(rows):
            for columnIdx in range(columns):
                # to start traversal:
                # (1) cell must be land
                # (2) cell must not be visited
                if grid[rowIdx][columnIdx] == self.land and not visited[rowIdx][columnIdx]:
                    self.traverse(rowIdx, columnIdx, grid, visited)
                    islands += 1
        return islands
```


## правильное решение (BFS: iterative (queue))
```python
class Solution:
    # land and water definition
    land, water = "1", "0"

    # down, left, up, right
    # coordinate: (rowIdx, columnIdx)
    steps = [
        (+1, 0),
        (0, -1),
        (-1, 0),
        (0, +1),
    ]

    def cell_is_in_boundaries(
        self, rowIdx: int, columnIdx: int, grid: list[list[str]]
    ) -> bool:
        rows, columns = len(grid), len(grid[0])
        return 0 <= rowIdx < rows and 0 <= columnIdx < columns

    def traverse(
        self, rowIdx: int, columnIdx: int, grid: list[list[str]], visited: list[list[bool]]
    ) -> None:
        queue = deque([(rowIdx, columnIdx)])
        visited[rowIdx][columnIdx] = True

        while queue:
            rowIdx, columnIdx = queue.popleft()
            for step in self.steps:
                nextRowIdx, nextColumnIdx = rowIdx + step[0], columnIdx + step[1]
                if (
                    not self.cell_is_in_boundaries(nextRowIdx, nextColumnIdx, grid)
                    or visited[nextRowIdx][nextColumnIdx]
                    or grid[nextRowIdx][nextColumnIdx] == self.water
                ):
                    continue
                queue.append((nextRowIdx, nextColumnIdx))
                visited[nextRowIdx][nextColumnIdx] = True

    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        rows, columns = len(grid), len(grid[0])
        visited = [[False for _ in range(columns)] for _ in range(rows)]

        for rowIdx in range(rows):
            for columnIdx in range(columns):
                # to start traversal:
                # (1) cell must be land
                # (2) cell must not be visited
                if grid[rowIdx][columnIdx] == self.land and not visited[rowIdx][columnIdx]:
                    self.traverse(rowIdx, columnIdx, grid, visited)
                    islands += 1
        return islands
```