**https://www.algoexpert.io/questions/optimal-freelancing**

## правильное решени
```python
def optimalFreelancing(jobs):
    LENGHT_OF_WEEK = 7
    profit = 0
    timeline = [False] * LENGHT_OF_WEEK

    # sort jobs by price in descending order
    # we need the highest jobs first
    jobs.sort(key=lambda job: job["payment"], reverse=True)
    # traverse jobs from highest to lowest paid
    # try to put appropriate job to the timeline
    # we would like to put the job at the latest timeline slot
    for job in jobs:
        """
        T T F F F F F
        1 2 3 4 5 6 7
        
        deadline = 2
        lenght_of_week = 7
        """
        maxTime = min(job["deadline"], LENGHT_OF_WEEK)  # what is the latest we might consider doing this job
        for timelineIdx in reversed(range(maxTime)):
            if timeline[timelineIdx] is False:
                timeline[timelineIdx] = True
                profit += job['payment']
                break
    return profit
```

## оценку по времени и памяти
- Time  O(n*log(n))
- Space O(1)

## идея
В первую очередь обратим внимание на:
    - у нас есть всего 7 дней для работы
    - каждая работа занимает ровно 1 день
    - дедлайн - хитрое определение того, в какой из семи дней работа может быть завершена

Сначала мы отсортируем работы по цене (от самой высокой до самой низкой). Далее, итерируясь по работам (от самой высокой до самой низкой) мы смотрим на дедлайн этой работы и сравниваем его с нашим таймлайном недели, а именно, в какой максимально поздний день мы можем поставить дедлайн (для этого используем timeline массив из False, помечая подходящий день True).