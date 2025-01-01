**https://leetcode.com/problems/surrounded-regions/description/**

## правильное решение (mine)
```python
from typing import List

class Solution:
    land, water = "O", "X"
    steps = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]

    def cell_is_in_boundaries(
        self, rowIdx: int, columnIdx: int, board: List[List[str]]
    ) -> bool:
        rows, columns = len(board), len(board[0])
        return 0 <= rowIdx < rows and 0 <= columnIdx < columns

    def traverse(
        self, rowIdx: int, columnIdx: int, board: List[List[str]], visited: List[List[bool]], swap: bool
    ) -> None:
        # Check if the current cell is invalid
        if (
            not self.cell_is_in_boundaries(rowIdx, columnIdx, board)
            or visited[rowIdx][columnIdx] is True
            or board[rowIdx][columnIdx] == self.water
        ):
            return

        # Mark the current cell as visited
        visited[rowIdx][columnIdx] = True
        if swap:
            # Perform the swap "O"->"X" if required
            board[rowIdx][columnIdx] = self.water

        # Recursively traverse all neighbors
        for step in self.steps:
            nextRowIdx, nextColumnIdx = rowIdx + step[0], columnIdx + step[1]
            self.traverse(
                nextRowIdx, nextColumnIdx, board, visited, swap
            )

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, columns = len(board), len(board[0])
        visited = [[False for _ in range(columns)] for _ in range(rows)]

        # Traverse the outer board
        for columnIdx in range(columns):
            self.traverse(0, columnIdx, board, visited, swap=False) # Top row
            self.traverse(rows - 1, columnIdx, board, visited, swap=False) # Bottom row

        for rowIdx in range(rows):
            self.traverse(rowIdx, 0, board, visited, swap=True) # Left column
            self.traverse(rowIdx, columns - 1, board, visited, swap=False) # Right column

        # Traverse the inner board
        for rowIdx in range(1, rows - 1):
            for columnIdx in range(1, columns - 1):
                self.traverse(rowIdx, columnIdx, board, visited, swap=True)
```

## правильное решение (not mine)
```python
class Solution:
    # проверяем не выходят ли индексы за границу массива, True - если не выходим
    def good_idx(self, i: int, j: int, board: list[list[str]]) -> bool:
        return 0 <= i < len(board) and 0 <= j < len(board[0])

    # делаем обход и помечаем вершины пройденными
    # если flip -> true, то помечаем все пройденные вершины как X
    def dfs(self, startX: int, startY: int, visited: list[list[bool]], board: list[list[str]], flip: bool):
        if not self.good_idx(startX, startY, board):
            return
        # dfs запускаем только для не посещенных вершин
        if visited[startX][startY] or board[startX][startY] == 'X':
            return

        visited[startX][startY] = True
        if flip:
            board[startX][startY] = 'X'

        steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # перебераем шаги которые могут быть из текущий вершины
        for step in steps:
            # вычисляем координаты куда можем пойти
            newX, newY = startX + step[0], startY + step[1]
            self.dfs(newX, newY, visited, board, flip)

    def solve(self, board: list[list[str]]) -> None:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        # перебираем крайние строки
        for i in range(len(board)):
            self.dfs(i, 0, visited, board, False)
            self.dfs(i, len(board[0]) - 1, visited, board, False)

        # перебираем крайние столбцы
        for i in range(len(board[0])):
            self.dfs(0, i, visited, board, False)
            self.dfs(len(board) - 1, i, visited, board, False)

        # обходим все индексы кроме крайних - т к их уже обходили
        for i in range(1, len(board) - 1):
            for j in range(1, len(board[i]) - 1):
                # bfs запускаем только для не посещенных вершин - проверка внутри
                self.dfs(i, j, visited, board, True)
```

## идея
```text
conceptual:
    также как и в классичкской задаче "number of islands", пользуемся dfs обходом и матрицей visited.
    дополнительно, нам понадобиться сначала обойти границы нашей борды ()


detailed:
    firstly we gonna traverse "outter" board (boundaries of board),
    whereas the goal of the traverse is to detect such islands, 
    which eventually touch the boundaries (how: by marking those as "X")

    afterwards, we gonna traverse "inner" board, marking adjacent islands as "X",
    for traversal we might use recursive DFS traversal, with directions as left, right, up, down
    additionaly, each cell we will check whether it is in boundaries of board itself
    eventhough we well inplace modify board itself, we also will define visited array of m*n to manage which cells were already visisted

Time  O(n*m)
Space O(n*m)
```