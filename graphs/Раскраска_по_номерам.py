"""
Дана раскраска по номерам в виде двумерного массива grid.
Нужно определить минимальное количество заливок, необходимых, чтобы «закрасить» всю картину.

Когда мы делаем «заливку» (например, в графическом редакторе), мы выбираем клетку,
и одновременно «заливаются» все соседние клетки того же цвета. Соседними считаем клетки сверху, снизу, слева и справа.

Ввод: grid =
[[1,1,1,1,1,1,1,1]
,[1,2,2,1,1,2,2,1]
,[1,2,1,2,2,1,2,1]
,[1,2,2,2,2,2,2,1]
,[1,1,1,1,1,1,1,1]]
Вывод: 4

Рассуждение
    у нас есть матрица, состоящая из клеток разных цветов
    клетки одного цвета соеденены (сверху, справа, снизу, слева)
    таким образом получаются связные компоненты

    Значит задача сводится к
        посчитать кол-во компонент связности в матрице, где связь определятеся цветом

    Решается через DFS/BFS по матрице

Алгоритм
    проходим по каждоый клетки
    если клетка еще не посещена
        запускаем DFS/BFS
        заливаем всю компоненту
        увеличиваем счетчик компонент
    возвразаем количество таких запусков
"""

from collections import deque


class ConnectedComponents:
    def in_bound(self, grid: list[list[int]], row: int, column: int) -> bool:
        return 0 <= row < len(grid) and 0 <= column < len(grid[row])

    def dfs_recursive(
        self,
        grid: list[list[int]],
        visited: list[list[bool]],
        row: int,
        column: int,
        color: int,
    ):
        if (
            not self.in_bound(grid, row, column)
            or visited[row][column]
            or grid[row][column] != color
        ):
            return

        visited[row][column] = True
        neighbours = [
            (row - 1, column),
            (row, column + 1),
            (row + 1, column),
            (row, column - 1),
        ]
        for nr, nc in neighbours:
            self.dfs_recursive(grid, visited, nr, nc, color)

    def dfs_iterative(
        self,
        grid: list[list[int]],
        visited: list[list[bool]],
        row: int,
        column: int,
        color: int,
    ):
        stack: deque[tuple[int, int]] = deque([(row, column)])
        while stack:
            row, column = stack.pop()

            neighbours = [
                (row - 1, column),
                (row, column + 1),
                (row + 1, column),
                (row, column - 1),
            ]

            if visited[row][column]:
                continue

            visited[row][column] = True

            for nr, nc in neighbours:
                if (
                    self.in_bound(grid, nr, nc)
                    and not visited[nr][nc]
                    and grid[nr][nc] == color
                ):
                    stack.append((nr, nc))


def draw_iterative(grid: list[list[int]]):
    graph = ConnectedComponents()
    visited: list[list[bool]] = [[False for _ in range(len(r))] for r in grid]
    components: int = 0

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if not visited[row][column]:
                graph.dfs_iterative(grid, visited, row, column, grid[row][column])
                components += 1
    return components


def draw_recursive(grid: list[list[int]]):
    graph = ConnectedComponents()
    visited: list[list[bool]] = [[False for _ in range(len(r))] for r in grid]
    components: int = 0

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if not visited[row][column]:
                graph.dfs_recursive(grid, visited, row, column, grid[row][column])
                components += 1
    return components


def test_dfs_recursive():
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 1, 1, 2, 2, 1],
        [1, 2, 1, 2, 2, 1, 2, 1],
        [1, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]
    result = draw_recursive(grid)
    assert result == 4, f"expected: 4, got {result}"


def test_dfs_iterative():
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 1, 1, 2, 2, 1],
        [1, 2, 1, 2, 2, 1, 2, 1],
        [1, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]
    result = draw_iterative(grid)
    assert result == 4, f"expected: 4, got {result}"


if __name__ == "__main__":
    test_dfs_recursive()
