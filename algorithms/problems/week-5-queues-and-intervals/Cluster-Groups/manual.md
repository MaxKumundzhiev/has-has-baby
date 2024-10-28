**private**

## условие
Дан массив возрастов пользователей ВК. Нужно определить сколько пользователей входят в каждую группу.

Input:
ages = [2, 4, 4, 35, 23, 12, 14, 36]
groups = [[1, 100], [2, 4], [12, 12], [100, 1000]]

Output:
[8, 3, 0, 1]

## правильное решени
```python
class Solution:
    def cluster_users(users: List[int], groups: List[int]):
        _agreed_bound_age = 100
        # compose an ages count array
        age_counter = [0 for _ in range(_agreed_bound_age)]
        for age in ages:
            age_counter[age] += 1
        
        # compose a suffix age array
        age_suffix = [0 for _ in range(_agreed_bound_age)]
        for age, count in enumerate(reversed(age_counter)):
            # first lookup
            if age == len(age_counter):
                age_suffix[age] = count
            else:
                previous_group_age_count = age_suffix[age+1]
                age_suffix[age] = previous_group_age_count + count
        
        # compose count per groups
        clusters = []
        for group in groups:
            start_age, end_age = group[0], group[1]
            # manage right boundary, by problme statement, right boundary might exceed real age
            if end_age > len(age_suffix):
                counter = age_suffix[start_age] - 0
            else:
                counter = age_suffix[start_age] - age_suffix[end_age]
            clusters.append(counter)
        
        return clusters
```

## оценку по времени и памяти
- Time O(n+m)
- Space O(n)

## путь по которому вы пришли к решению

## идея
- сделать массив счетчика возрастов по массиву возрастов (*уточнив масимальный возраст)
- сделать суффиксный массив возрастов по массиву счетчика возрастов (итерируемся справа налево)
- по формуле префиксных массивов считаем кол-во человек в группе
