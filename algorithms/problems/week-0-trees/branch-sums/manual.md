**https://www.algoexpert.io/questions/branch-sums**

## правильное решени
```python
def branchSums(root):
    def traverse(node, sums, currSum):    
        if not node:
            return
        
        currSum += node.value
        if not node.left and not node.right:
            sums.append(currSum)
            return
            
        traverse(node=node.left, sums=sums, currSum=currSum)
        traverse(node=node.right, sums=sums, currSum=currSum)

    sums = []
    traverse(node=root, sums=sums, currSum=0)
    return sums

```

## оценку по времени и памяти
- Time  O(n)
- Space O(n)

## идея
```text
use preorder recursive traverse, make sure to add condition to check node does not have both left and right children, what says its termination node and we need to add branch sum to result 
```
