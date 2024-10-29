**https://leetcode.com/problems/valid-sudoku/description/**

## правильное решени
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, columns, blocks = set(), set(), set()
        rows_, columns_ = 9, 9
        empty_cell, sub_box_offset = ".", 3

        for rowIdx in range(rows_):
            for columnIdx in range(columns_):
                cell = board[rowIdx][columnIdx]
                if cell == empty_cell:
                    continue
                blockIdx = rowIdx // sub_box_offset * sub_box_offset + columnIdx // sub_box_offset
                cell_seen_in_row = True if (rowIdx, cell) in rows else False
                cell_seen_in_column = True if (columnIdx, cell) in columns else False
                cell_seen_in_block = True if (blockIdx, cell) in blocks else False

                if cell_seen_in_row or cell_seen_in_column or cell_seen_in_block:
                    return False
                rows.add((rowIdx, cell))
                columns.add((columnIdx, cell))
                blocks.add((blockIdx, cell))
        return True
```

## оценку по времени и памяти
- Time  O(1)
- Space O(1)

## путь по которому вы пришли к решению
Разбор

## идея
- Заведем 3 хэш сета, для строк, для столбцов и для блока
    - для строки: (rowIdx, value)
    - для столюца: (columnIdx, value)
    - для блока: (blockIdx, value)
        - для blockIdx: rowIdx // 3 * 3 + columnIdx // 3
- Начинаем итерироваться слева направо сверзу вниз
- На каждой интерации проверяем, пустая / не пустая клетка
    - Если пустая, переходим на следуюзую клетку
    - Если не пустая, то проверяем
        - не встречали ли мы такое значение в строках уже
        - не встречали ли мы такое значение в столбцах уже
        - не встречали ли мы такое значение в блоке уже