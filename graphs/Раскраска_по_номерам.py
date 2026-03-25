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


def recursive_dfs(grid: list[list[int]]):
    def in_bound(grid: list[list[int]], row: int, column: int) -> bool:
        return 0 <= row < len(grid) and 0 <= column < len(grid[row])

    def dfs(
        grid: list[list[int]],
        visited: list[list[bool]],
        color: int,
        row: int,
        column: int,
    ) -> None:
        # check if cell is in bound
        # check if cell was not visited before
        # check if cell is same color as previous
        if (
            not in_bound(grid, row, column)
            or visited[row][column]
            or grid[row][column] != color
        ):
            return

        # mark cell as visited
        visited[row][column] = True
        # traverse neighbours
        neigbours: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dx, dy in neigbours:
            dfs(grid, visited, color, row + dx, column + dy)

    visited: list[list[bool]] = [[False for _ in range(len(r))] for r in grid]
    components: int = 0

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if not visited[row][column]:
                dfs(grid, visited, grid[row][column], row, column)
                components += 1
    print(components)
    return components


def test_dfs_recursive():
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 1, 1, 2, 2, 1],
        [1, 2, 1, 2, 2, 1, 2, 1],
        [1, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]
    assert recursive_dfs(grid) == 4
    assert recursive_dfs(grid=[]) == 0


if __name__ == "__main__":
    test_dfs_recursive()
