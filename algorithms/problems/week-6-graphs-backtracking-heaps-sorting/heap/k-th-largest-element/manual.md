**https://leetcode.com/problems/kth-largest-element-in-an-array/**

## правильное решение
```python
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min-heap with the first k elements of the array
        min_heap = nums[:k]
        heapq.heapify(min_heap)
    
        # Iterate through the remaining elements in the array
        for num in nums[k:]:
            if num > min_heap[0]:  # Compare with the smallest element in the heap
                heapq.heappop(min_heap)  # Remove the smallest element
                heapq.heappush(min_heap, num)  # Add the current element
        
        # The root of the heap (min_heap[0]) is the Kth largest element
        return min_heap[0]
```

### Explanation:
1. **Heap Initialization**: A min-heap of size `k` is created using the first `k` elements of the array.
2. **Heap Maintenance**: For each element beyond the first `k` elements, if it is larger than the smallest element in the heap (root), it replaces the root. This maintains the property that the heap contains the `k` largest elements seen so far.
3. **Result**: After processing all elements, the root of the heap is the `k`th largest element.

### Complexity:
- **Time Complexity**:
  - Building the heap: \(O(k)\)
  - For the remaining \(n-k\) elements: \(O((n-k) \log k)\)
  - Total: \(O(n \log k)\)
- **Space Complexity**: \(O(k)\) for the heap.