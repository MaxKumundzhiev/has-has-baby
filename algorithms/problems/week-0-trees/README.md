## Деревья
- Деревья это структура данных, которая состоит из узлов (nodes). Каждый узел будет иметь одну или несколько ссылок на их детские ноды.
```python
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
```

## Деревья Поиска (BST - Binary Search Tree)
Деревья Поиска - это структура данных, которая состоит из узлов (nodes). Каждый узел будет иметь 1 или 2 ссылки на детские ноды. Главное свойство BST, для каждой вершины:
- слева меньше
- справа больше
- вершина удовлетворяет условию: `low < node.val < high`
```
example:
        10
       /  \
      5   11
     / \    \
   -2   7   15

property
    left:   subtree: -2 < 5  | 5 < 7 < 10 | 5 < 10
    right:  subtree: 15 > 11 | 11 > 10 
```

### Важные свойства Бинарного Дерева Поиска (BST)
- `центрированный обход` (inorder traverse) и `left -> node -> right` - дает `отсортированный по возрастанию порядок` элементов.
- `центрированный обход` (inorder traverse) и `right -> node -> left` - дает `отсортированный по убыванию порядок` элементов.
- `самое минимально значение хранится в самой левой ноде дерева`
```python
current = root
while current:
    current = current.left
```
- `самое максимальное значение хранится в самой правой ноде дерева`
```python
current = root
while current:
    current = current.right
```
- `сбалансированное дерево` - когда для каждого поддерева верно утверждение, что высота левого и правого поддерева отличается не более чем 1 `(asb(leftTreeHeight - rightTreeHeight)) ≤ 1`
- когда формируем бинарное дерево из массива, нужно помнить как находить индексы:
```python
- первый элемент массива - корень
- левый ребенок имеет индекс: i * 2 + 1, где i - индекс вершины в массиве root
- правой ребенок имеет индекс: i * 2 + 2, где i - индекс вершины в массиве root
- если значение null или *индекс вершины выходит за границы массива*, то вершина отсутствует
```


## Способы обхода дерева
1. Обход в глубину (DFS)
    - preorder
    - inorder
    - postorder
2. Обход в ширину (BFS)
    - level order

**Заметка**
- Обход в глубину (DFS) 
    - реализуется итеративно и рекурсивно
    - когда реализуется итеративно - используется stack и порядок LIFO (добавляется в конец, спимается с конца)
- Обход в ширину (BFS)
    - реализуется итеративно
    - когда реализуется итеративно - используется queue и порядок FIFO (добавляется в конец, спимается с начала)


## Существуют алгоритмы балансировки деревьев
 - Red Black Trees
 - AVL Trees


## Референсы
- https://right-lupin-f79.notion.site/Python-955206472c7e46f3982f6337ce1cc85d


## Задачи
<img width="878" alt="Screenshot 2024-12-28 at 16 15 26" src="https://github.com/user-attachments/assets/f512fae2-1bb5-4a12-a87a-f33360a6fab1" />
<img width="871" alt="Screenshot 2024-12-28 at 16 15 39" src="https://github.com/user-attachments/assets/6e538f25-b509-4d95-9fdc-db187233e03c" />
<img width="875" alt="Screenshot 2024-12-28 at 16 15 55" src="https://github.com/user-attachments/assets/7aaef336-941d-430f-9dda-efbf0cac5efc" />
<img width="879" alt="Screenshot 2024-12-28 at 16 16 11" src="https://github.com/user-attachments/assets/420516c1-8ce0-4289-aa6e-a375f9fdd41d" />
<img width="874" alt="Screenshot 2024-12-28 at 16 16 28" src="https://github.com/user-attachments/assets/8695cc71-86b7-4fd1-86f1-4dc1fa178547" />
<img width="875" alt="Screenshot 2024-12-28 at 16 16 40" src="https://github.com/user-attachments/assets/7dbfa867-6faf-4719-bd1c-743ee22fab54" />
<img width="880" alt="Screenshot 2024-12-28 at 16 17 02" src="https://github.com/user-attachments/assets/6c29a614-3416-4428-8423-611032140571" />
<img width="875" alt="Screenshot 2024-12-28 at 16 18 52" src="https://github.com/user-attachments/assets/3fdebc91-7471-496a-917f-008afa508ff4" />








