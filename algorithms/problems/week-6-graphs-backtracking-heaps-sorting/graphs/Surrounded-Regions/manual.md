**https://leetcode.com/problems/surrounded-regions/description/**

## правильное решени
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

## оценку по времени и памяти
- Time: O(n*m)
- Space: O(n*m)

## путь по которому вы пришли к решению
```
начинаем итерироваться слева направо сверзу вниз до тех пор пока не найдем клетку "O"
как только нашли клетку "O" - запускаем рекурсивный поиск в глубину (DFS)
    проверяем если клетка в границах
    и
    проверяем если клетка "O"
    помечаем клетку как "X"

    запускаем поиск вниз
    запускаем поиск влево
    запускаем поиск вверх
    запускаем поиск вправо 
```
```python
class Solution:
    steps = {
        "left": [0, -1],
        "right": [0, 1],
        "up": [-1, 0],
        "down": [1, 0]
    }

    def in_boundaries(self, rowIdx, columnIdx, board):
        return 0 <= rowIdx < len(board) and 0 <= columnIdx < len(board[0])
    
    def on_edge(self, rowIdx, columnIdx, board):
        return True if rowIdx == len(board)-1 or columnIdx == len(board[0])-1 else False

    def dfs(self, rowIdx, columnIdx, board):
        cell_in_boundaries = self.in_boundaries(rowIdx, columnIdx, board)
        cell_is_region = board[rowIdx][columnIdx] == "O"
        cell_on_edge = self.on_edge(rowIdx, columnIdx, board)

        # check if cell is appropriate
        if not cell_in_boundaries or not cell_is_region or cell_on_edge:
           return
        
        # mark cell as "visited" which is equal to "X"
        board[rowIdx][columnIdx] = "X"
        # down
        self.dfs(
            rowIdx + self.steps['down'][0], columnIdx + self.steps['down'][1], board
        )
        # left
        self.dfs(
            rowIdx + self.steps['left'][0], columnIdx + self.steps['left'][1], board
        )
        # up
        self.dfs(
            rowIdx + self.steps['up'][0], columnIdx + self.steps['up'][1], board
        )
        # right
        self.dfs(
            rowIdx + self.steps['right'][0], columnIdx + self.steps['right'][1], board
        )

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, columns = len(board), len(board[0])
        
        for rowIdx in range(rows):
            for columnIdx in range(columns):
                cell = board[rowIdx][columnIdx]
                if cell == "O":
                    self.dfs(rowIdx, columnIdx, board)
        return
```

## идея