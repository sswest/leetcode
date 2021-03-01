## 解题思路

### 递归

链表节点俩俩交换，对于任意一节节点交换过程如下:

```python
temp = head.next
head.next = Swap(temp.next)
head = temp
```

递归该过程，递归结束条件为传入节点为空或者传入节点为最后一个节点。

时间复杂度O(n)
