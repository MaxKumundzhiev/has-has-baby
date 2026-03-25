"""
Дан корень бинарного дерева. Нужно вернуть сумму всех правых листьев в дереве. Если правых листьев нет, то нужно вернуть ноль
ВАЖНО: реши задачу с использованием рекурсии


Размышления
    воспользуемся паттерном снизу вверх так как требуется сумма листьев
    также будем использовать preoprder dfs (хотя можем воспользуеться любым обходом)

    на базовом случае будем проверять на сузествование ноды и возвразать 0
    в целом будем проверять что нода это лист и является правым ребенком через прокидывание флага от родителя флага
"""

from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def dfs(node: Optional[TreeNode], is_right: bool) -> int:
    if not node:
        return 0

    if not node.left and not node.right and is_right:
        return node.val

    return dfs(node.left, False) + dfs(node.right, True)
