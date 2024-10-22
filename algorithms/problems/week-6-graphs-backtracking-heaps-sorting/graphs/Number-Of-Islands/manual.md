**https://leetcode.com/problems/number-of-islands/description/**

## правильное решени
```python
class Solution:
    def dfs(self, rowIdx, columnIdx, used, grid):
        rows, columns = len(grid), len(grid[0])

        if (0 <= rowIdx < rows) \
            and (0 <= columnIdx < columns) \
            and not used[rowIdx][columnIdx] \
            and grid[rowIdx][columnIdx] == "1":
            
            used[rowIdx][columnIdx] = True
            steps = [
                [1, 0], [0, -1],
                [-1, 0], [0, 1]
            ]
            for step in steps:
                next_rowIdx, next_columnIdx = rowIdx + step[0], columnIdx + step[1]
                self.dfs(next_rowIdx, next_columnIdx, used, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        used = [[False for _ in range(columns)] for row in range(rows)]
        result = 0

        for rowIdx in range(rows):
            for columnIdx in range(columns):
                if grid[rowIdx][columnIdx] == "1" and not used[rowIdx][columnIdx]:
                    self.dfs(rowIdx, columnIdx, used, grid)
                    result += 1

        return result
```

## оценку по времени и памяти
- Time: O(V + E)
- Space: O(V)

## путь по которому вы пришли к решению
- разбор + доп материалы

## идея

## реализации

### DFS рекурсивное
```python
class Solution:
    _steps = {
        "down": [1, 0],
        "left": [0, -1],
        "up": [-1, 0],
        "right": [0, 1]
    }

    def is_in_boundaries(self, rowIdx, columnIdx, grid):
        return 0 <= rowIdx < len(grid) and 0 <= columnIdx < len(grid[0])

    def get_next_idx(self, current, add):
        return current + add

    def dfs(self, rowIdx, columnIdx, grid, used):
        cell_is_in_boundaries = self.is_in_boundaries(rowIdx=rowIdx, columnIdx=columnIdx, grid=grid)
        if not cell_is_in_boundaries:
            return

        cell_is_land = True if grid[rowIdx][columnIdx] == "1" else False
        cell_is_visited = True if used[rowIdx][columnIdx] is True else False
        if not cell_is_land or cell_is_visited:
            return
        else:
            used[rowIdx][columnIdx] = True
            self.dfs(
                rowIdx=self.get_next_idx(current=rowIdx, add=self._steps["down"][0]),
                columnIdx=self.get_next_idx(current=columnIdx, add=self._steps["down"][1]), 
                grid=grid, 
                used=used
            )
            self.dfs(
                rowIdx=self.get_next_idx(current=rowIdx, add=self._steps["left"][0]),
                columnIdx=self.get_next_idx(current=columnIdx, add=self._steps["left"][1]), 
                grid=grid, used=used
            )
            self.dfs(
                rowIdx=self.get_next_idx(current=rowIdx, add=self._steps["up"][0]),
                columnIdx=self.get_next_idx(current=columnIdx, add=self._steps["up"][1]), 
                grid=grid, 
                used=used
            )
            self.dfs(
                rowIdx=self.get_next_idx(current=rowIdx, add=self._steps["right"][0]),
                columnIdx=self.get_next_idx(current=columnIdx, add=self._steps["right"][1]),
                grid=grid, 
                used=used
            )

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        used = [[False for _ in range(columns)] for _ in range(rows)]
        islands = 0

        for rowIdx in range(rows):
            for columnIdx in range(columns):
                cell_is_land = True if grid[rowIdx][columnIdx] == "1" else False
                cell_is_visited = True if used[rowIdx][columnIdx] is True else False

                if cell_is_land and not cell_is_visited:
                    self.dfs(
                        rowIdx=rowIdx, columnIdx=columnIdx, grid=grid, used=used
                    )
                    islands += 1
        return islands
```

### DFS итеративное
```python
from collections import deque 

class Solution:
    def is_in_boundaries(self, rowIdx, columnIdx, grid):
        return 0 <= rowIdx < len(grid) and 0 <= columnIdx < len(grid[0])

    def dfs(self, rowIdx, columnIdx, grid, used):
        queue = deque([(rowIdx, columnIdx)])
        used[rowIdx][columnIdx] = True

        while bool(queue) is True:
            rowIdx, columnIdx = queue.pop()
            steps = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            for step in steps:
                next_rowIdx, next_columnIdx = rowIdx + step[0], columnIdx + step[1]
                if not self.is_in_boundaries(rowIdx=next_rowIdx, columnIdx=next_columnIdx, grid=grid):
                    continue
                
                cell_is_land = True if grid[next_rowIdx][next_columnIdx] == "1" else False
                cell_is_visited = True if used[next_rowIdx][next_columnIdx] is True else False
                if not cell_is_land or cell_is_visited:
                    continue
        
                queue.append([next_rowIdx, next_columnIdx])
                used[next_rowIdx][next_columnIdx] = True

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        used = [[False for _ in range(columns)] for _ in range(rows)]
        islands = 0

        for rowIdx in range(rows):
            for columnIdx in range(columns):
                cell_is_land = True if grid[rowIdx][columnIdx] == "1" else False
                cell_is_visited = True if used[rowIdx][columnIdx] is True else False

                if cell_is_land and not cell_is_visited:
                    self.bfs(rowIdx=rowIdx, columnIdx=columnIdx, grid=grid, used=used)
                    islands += 1
        return islands
```


### BFS итеративно
```python
from collections import deque 

class Solution:
    def is_in_boundaries(self, rowIdx, columnIdx, grid):
        return 0 <= rowIdx < len(grid) and 0 <= columnIdx < len(grid[0])

    def bfs(self, rowIdx, columnIdx, grid, used):
        queue = deque([(rowIdx, columnIdx)])
        used[rowIdx][columnIdx] = True

        while bool(queue) is True:
            rowIdx, columnIdx = queue.popleft()
            steps = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            for step in steps:
                next_rowIdx, next_columnIdx = rowIdx + step[0], columnIdx + step[1]
                if not self.is_in_boundaries(rowIdx=next_rowIdx, columnIdx=next_columnIdx, grid=grid):
                    continue
                
                cell_is_land = True if grid[next_rowIdx][next_columnIdx] == "1" else False
                cell_is_visited = True if used[next_rowIdx][next_columnIdx] is True else False
                if not cell_is_land or cell_is_visited:
                    continue
        
                queue.append([next_rowIdx, next_columnIdx])
                used[next_rowIdx][next_columnIdx] = True

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        used = [[False for _ in range(columns)] for _ in range(rows)]
        islands = 0

        for rowIdx in range(rows):
            for columnIdx in range(columns):
                cell_is_land = True if grid[rowIdx][columnIdx] == "1" else False
                cell_is_visited = True if used[rowIdx][columnIdx] is True else False

                if cell_is_land and not cell_is_visited:
                    self.bfs(rowIdx=rowIdx, columnIdx=columnIdx, grid=grid, used=used)
                    islands += 1
        return islands
```
