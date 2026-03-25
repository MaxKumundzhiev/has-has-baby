"""
Дан корень бинарного дерева. Нужно вернуть сумму всех листьев в дереве
ВАЖНО: реши задачу с использованием рекурсии


Размышления
    нам нужна сумма всех листьев, значит используем паттерн снизу вверх
    снизу будем подымать сумму листьев навверх
    «Это postorder-подход (bottom-up), но порядок обхода не влияет, так как мы просто агрегируем значения.»
"""

from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def dfs(node: Optional[TreeNode]) -> int:
    if not node:
        return 0

    if not node.left and not node.right:
        return node.val

    return dfs(node.left) + dfs(node.right)


def main():
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    return dfs(root)
