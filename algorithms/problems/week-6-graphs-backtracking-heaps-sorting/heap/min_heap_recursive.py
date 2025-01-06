"""
Implement min heap data structure with following operations:
1. add value to heap
2. peek min element
3. delete min element
4. heapify
"""


class MinHeap:
    def __init__(self):
        self.array = []

    def shiftUp(self, idx: int):
        """
        Method, which is meant to shift a value up within a given idx.
        Notes:
            Method works as follows:
            1. Compose a parent idx for a given idx
            2. Check condition parentValue > currentValue (for MinHeap, meaning, shift up smaller value)
            3. If condition compiled, swap values 
            4. Continue shiftUp passing parentIdx
        """
        # sanity check for allowed value type
        if not isinstance(idx, int):
            raise TypeError
        
        # look up the state of dynamic array (heap)
        is_empty = True if bool(self.array) is False else False
        if is_empty:
            raise Exception
        
        # base case for return when idx is zero
        if idx == 0: 
            return

        parentIdx = (idx - 1) // 2
        # shift up will be performed
        # just and only if parent value is grater than current value
        # pay attention, self.array[parentIdx] > self.array[idx] is for MinHeap
        # pay attention, self.array[parentIdx] < self.array[idx] is for MaxHeap
        if self.array[parentIdx] > self.array[idx]:
            # swap the value and continue shiftUp
            self.array[idx], self.array[parentIdx] = self.array[parentIdx], self.array[idx]
            self.shiftUp(idx=parentIdx)

    def shiftDown(self, idx):
        # sanity check for allowed value type
        if not isinstance(idx, int):
            raise TypeError
        
        # look up the state of dynamic array (heap)
        is_empty = True if bool(self.array) is False else False
        if is_empty:
            raise Exception
        
        leftIdx, rightIdx = (idx*2)-1, (idx*2)-2
        # base case for return when left idx is grater than len of array
        if leftIdx >= len(self.array):
            return
        
        # prepare ...
        # @TODO: finish shift down logic
    
    def add(self, value: int) -> None:
        """
        Method, which is meant to add a value to heap.
        Notes:
            Method works as follows:
                1. add value to the end of dynamic array;
                2. launch shiftUp method until heap conditions are complied;
        """
        # sanity check for allowed value type
        if not isinstance(value, int):
            raise TypeError

        # look up the state of dynamic array (heap)
        is_empty = True if bool(self.array) is False else False
        # add value to the heap independently of its state
        self.array.append(value)
        # edge case if array (heap) is empty, means no need to use shiftUp
        if not is_empty:
            # the value at the -1 index - because the new value is stored at the end of array
            lastIdx = len(self.array)-1
            self.shiftUp(idx=lastIdx)
        return

    def peek_min(self) -> int | None:
        """
        Method, which is meant to peek a min value.
        """
        # look up the state of dynamic array (heap)
        is_empty = True if bool(self.array) is False else False
        # heap is empty, there is no min value, thus return None
        if is_empty:
            return
        # heap is not empty, there is min value, which is stored at 0 idx
        return self.array[0]
    
    def delete_min(self) -> None:
        """
        Method, which is meant to delete the min value from heap.
        Notes:
            Method works as follows:
                1. swap the first and the last elements
                2. delete the last element
                3. launch shiftDown method for the first element, until heap conditions are complied;
        """
        # look up the state of dynamic array (heap)
        is_empty = True if bool(self.array) is False else False
        if is_empty:
            raise Exception
        
        elements_grater_than_one = True if len(self.array) > 1 else False
        # if heap contains > 1 element
        # need to perform swap, delete and shiftDown operations
        # otherwise, only delete operation
        # however, in both cases, we need to perform delete operation
        if elements_grater_than_one:
            self.array[0], self.array[-1] = self.array[-1], self.array[0]
        self.array.pop()
        if elements_grater_than_one:
            # the value at the 0 index - because the value to shift down is stored at the beginning of array
            firstIdx = 0
            self.shiftDown(idx=firstIdx)
        return