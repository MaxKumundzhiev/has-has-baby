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

### DFS итеративное

### BFS рекурсивное
