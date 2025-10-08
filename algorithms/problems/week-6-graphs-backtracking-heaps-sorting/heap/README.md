## Heap
Куча - реализуется через структуру данных дерево (`не путать со свойствами бинарного дерева поиска`)

Куча может применяться в следующих задачах:
1. найти K (наибольших | наименьших) элементов
2. найти K-ый (наибольшый | наименьший) элемент


Свойства кучи:
- каждый ребенок - это и есть куча, то есть свойства будут распространяться на каждое поддерево
- для текущего элемента работает правило: 
    - `все что внизу - оно меньше` (для макс кучи)
    - `все что внизу - оно больше` (для мин кучи)
- куча гарантирует:
    - `в самом верху самый наибольший элемент` (для макс кучи)
    - `в самом верху самый наименьший элемент` (для мин кучи)


Основные операции кучи:
- положить в кучу X
- достать самый большой | маленький элемент
- удалить самый большой | маленький элемент
- heapify - это процедура, которая позволяет из массива сделать куча на максимум или на минимум
- дополнительно:
    - siftUp
    - siftDown


## Реализация
Кучу обычно реализуют на динамическом массиве.

- sifttUp (просеять наверх) (time O(log(n)))
```text
помним, что у нас есть динамический массив, где мы храним все элменты кучи.
просеять вверх - это означает довести элемент вверх, чтобы выполнялись все свойства кучи.

как работает
1. находим индекс родителя:
    parentIdx = (idx-1) // 2
2. заходим в родителя и проверяем, если:
    parentValue = array[parentIdx]
    для max heap:
        if currentValue > parentValue:
            array[idx], array[parentIdx] = parentValue, currentValue
    для min heap:
        if currentValue < parentValue:
            array[idx], array[parentIdx] = parentValue, currentValue
3. передвигаемся на родителя и запускаем такую же процедуру
```

- siftDown (просеять вниз) (time O(log(n)))
```text
помним, что у нас есть динамический массив, где мы храним все элменты кучи.
просеять вниз - это означает довести элемент вниз, чтобы выполнялись все свойства кучи.

как работает
1. находим индексы левого и правого детей:
    leftIdx = idx*2+1
    rightIdx = idx*2+2
2. заходим в детей и проверяем, если:
    leftValue = array[leftIdx]
    rightValue = array[rightIdx]
    
    # просеиваим вниз в сторону максимального элемента
    # ищем МАКСИМАЛЬНЫЙ элемент между детьми и просеиваем в сторону максимально
    для max heap:
        maxValue = max(leftValue, rightValue)
        # двигаемся влево
        if maxValue == leftValue:
            array[idx], array[leftIdx] = leftValue, currentValue
        # двигаемся вправо
        else:
            array[idx], array[rightIdx] = rightValue, currentValue

    # просеиваим вниз в сторону минимального элемента
    # ищем МИНИМАЛЬНЫЙ элемент между детьми и просеиваем в сторону минимального
    для min heap:
        minValue = min(leftValue, rightValue)
        # двигаемся влево
        if minValue == leftValue:
            array[idx], array[leftIdx] = leftValue, currentValue
        # двигаемся вправо
        else:
            array[idx], array[rightIdx] = rightValue, currentValue
3. передвигаемся на min | max ребенка и запускаем такую же процедуру 
```

- положить в кучу X (time O(log(n)))
```
помним, что у нас есть динамический массив, где мы храним все элменты кучи.
когда мы добавляем элемент - мы должны за константу добавить новый элемент X в конец массива и запустить просеивание элемента вверх
```

- достать самый большой | маленький элемент (time O(1))
```
помним, что у нас есть динамический массив, где мы храним все элменты кучи.
когда мы хотим самый большой или маленький элемент - мы знаем что этот элемент лежит в "корне" (под индексом 0 в куче) - и мы его возвращаем.
```

- удалить самый большой | маленький элемент (time O(log(n)))
```
помним, что у нас есть динамический массив, где мы храним все элменты кучи.
когда мы хотим удалить самый большой или маленький элемент:
1. мы меняем первый и последний элементы в динамическом массиве
2. запускаем shiftDown на первый элемент
```

- heapify (time O(n))
```
это процедура, которая позволяет из массива сделать куча на максимум или на минимум
рабоатет как: просеить все элементы вниз
```

**формулы для поиска индексов на массвие**
```text
leftChild = i*2 + 1
rightChild = i*2 + 2
parent = (i-1) // 2


## Общие заметки и реализация
```python
class MaxHeap:
    def __init__(self):
        self.container = []

    def __len__(self) -> int:
        return len(self.container)

    def __bool__(self) -> bool:
        return len(self.container) != 0

    # Time O(log(n))
    def insert(self, value: int) -> None:
        self.container.append(value)
        if len(self.container) > 1:
            idx = len(self.container) - 1
            self.sift_up(idx=idx)

    # Time O(log(n))
    def remove(self, idx: int) -> None:
        last_idx = len(self.container) - 1
        if idx == last_idx:
            self.container.pop()
            return

        self.container[idx], self.container[last_idx] = self.container[last_idx], self.container[idx]
        self.container.pop()
        # After swap & pop, decide to sift up or sift down:
        if idx < len(self.container):
            # Try sift down then sift up if needed:
            self.sift_down(idx=idx)
            self.sift_up(idx=idx)

    # Time O(1)
    def peek_top(self) -> int | None:
        if not self.container:
            return None
        return self.container[0]

    # Time O(log(n))
    def pop_top(self) -> int | None:
        if not self.container:
            return None

        first_idx, last_idx = 0, len(self.container) - 1
        top_value = self.container[first_idx]
        
        self.container[first_idx], self.container[last_idx] = self.container[last_idx], self.container[first_idx]
        self.container.pop(last_idx)

        if self.container:
            self.sift_down(idx=first_idx)
        
        return top_value

    # Time O(log(n))
    def sift_up(self, idx: int) -> None:
        top_idx, parent_idx, child_idx = 0, (idx - 1) // 2, idx
        child_value, parent_value = self.container[child_idx], self.container[parent_idx]

        # base case (1) element is top (root)
        if idx == top_idx:
            return None
        
        # base case (2) heap condition is satisfied
        # MaxHeap - parentValue >= childValue
        # MinHeap - parentValue <= childValue
        if parent_value >= child_value:
            return None

        # otherwise, continue siftUp procedure
        self.container[child_idx], self.container[parent_idx] = self.container[parent_idx], self.container[child_idx]
        self.sift_up(idx=parent_idx)
        return None

    # Time O(log(n))
    def sift_down(self, idx: int) -> None:
        bottom_idx = len(self.container) - 1
        left_child_idx, right_child_idx = 2 * idx + 1, 2 * idx + 2
        
        # Если нет потомков — заканчиваем
        if left_child_idx > bottom_idx:
            return
        
        # Находим индекс большего потомка (если есть правый)
        largest_child_idx = left_child_idx
        if right_child_idx <= bottom_idx and self.container[right_child_idx] > self.container[left_child_idx]:
            largest_child_idx = right_child_idx
        
        # Если текущий элемент меньше большего потомка — меняем и рекурсивно вызываем sift_down для потомка
        if self.container[idx] < self.container[largest_child_idx]:
            self.container[idx], self.container[largest_child_idx] = self.container[largest_child_idx], self.container[idx]
            self.sift_down(largest_child_idx)

        return None
```








```
