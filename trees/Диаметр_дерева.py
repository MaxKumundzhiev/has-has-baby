"""
Дан корень бинарного дерева root.
Нужно найти диаметр дерева — длину самого длинного пути между любыми двумя узлами.
Путь может не проходить через корень. Длина пути измеряется количеством рёбер.


     1
     |
     2
    / \
   3   4
  /     \
 5       6

Размышления
    обойти дерево снизу вверх - паттерн будет снизу вверх
    с нодами ничего не нужно делать поэтому обход может быть любым (но воспользуемя преордер рекурсивным)
    диаметр это максимальная сумма высоты левого и правого поддеревьев

    будем использовать замыкание (на переменной диаметр)
    подымаясь снизу вверх мы будем возвразать родителю максимальную глубину (высоту) из левого и правого поддеревьев
    в это же время на каждоый итерации обновлять диаметр как максимум между диаметром и суммой максимальных высот левого и правого поддеревьев
"""

from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def find_diameter(root: TreeNode) -> int:
    diameter: int = 0

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal diameter

        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    dfs(root)
    return diameter
