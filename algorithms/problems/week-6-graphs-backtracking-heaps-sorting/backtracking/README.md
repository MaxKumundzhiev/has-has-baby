## Backtracking
Backtracking - это тип задач про полный перебор, иными словами, где вас просят полностью что то перебрать (все возможные варианты).

Существуют 2 подхода решение
- рекурсивно
- не рекурсивно (рсновано на системах исчисления)

## Как обычно решается (рекурсивно)
- у нас всегда есть стартавая точка - с нее будет начинаться перебор
- у нас также есть состояние и переменные, которые описывают это состояние
- у нас рекурсивная функция, которая состоит из:
    - base case - 1 или несколько - это условия когда комбинация полностью собрана
    - основная логика backtracking-а
        - добавить в состояние
        - запустить рекурсивную генерацию
        - убрать из состояния



```python
class Solution:
    def backtraking(self, currentState, result, iterable):
        # base case(s)
        if ... # here we set our base case conditions - those, which identify, combination is composed
            # add that combination to result
            result.append(currentState)
            return
        
        # if not a base case, we kick off backtracking logic
        # update state --> recursive backtracking --> pop state (rollback to previous state)
        currentState.append(iterable)
        # assume, we updated currentState and itarable
        self.backtraking(currentState, result, iterable)
        # backtrack to previous state
        currentState.pop()
    
    def main(self, iterable):
        iterable, result = itarable, []
        self.backtraking(currentState=[], result=result, iterable=itarable)
        return result
    ...
```