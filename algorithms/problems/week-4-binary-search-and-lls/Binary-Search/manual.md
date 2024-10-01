**https://leetcode.com/problems/binary-search/description/**

## правильное решени
```python
class Solution:
    def good(self, number: int, target: int) -> bool:
        return number <= target

    def search(self, nums: list[int], target: int) -> int:
        answer = -1
        left, right = 0, len(nums)
        
        while right-left > 1:
            middle = (left+right) // 2
            is_good = self.good(number=nums[middle], target=target)
            if is_good:
                left = middle
            else:
                right = middle
        
        return left if nums[left] == target else answer
```

## оценку по времени и памяти
- Time: O(log(n))
- Space: O(1)

## путь по которому вы пришли к решению
При ипользовании бинарыого поиска, иы должны определиться с хорошим / плохим элементом. В нашем случае, хороший элемент это элмент, чье значени <= target, в ином случае плохой. Также, нужно понимать, что бинарный поиск остановит свою работу, когда left и right указатели будут указывать на последний хороший и плохой элменеты соответсвенно. В нашем случае, еще нужно проверить, что элменет на левом указатеое (последний хороший) равняется таргету, если не, значит target элемента нету.

## идея
Идея - бинарный поиск + переиспользовать стандартную реализацию (шаблон) бинарного поиска. 
