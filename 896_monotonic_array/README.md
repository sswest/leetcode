## 解题思路

单调数列对于`0<=i<=len(A)-1`一定会满足A<sub>i</sub> <= A<sub>i+1</sub> 或者 A<sub>i</sub> >= A<sub>i+1</sub>

单调递增和单调递减有不同的满足条件，因此应该先判断数列的单调性 

如果A<sub>0</sub> 大于 A<sub>1</sub> 那么数列单调递减

如果A<sub>0</sub> 小于 A<sub>1</sub> 那么数列单调递增

如果A<sub>0</sub> 等于 A<sub>1</sub> 那么数列单调性可能递增也可能递减。 这种情况下只能继续往后判断A<sub>i+1</sub>和A<sub>i</sub>的大小关系

```python
    i = 0
    while i < len(A) - 2 and A[i] == A[i + 1]:
        i += 1
    if i == len(A) - 1:  # 表示数列中的拥有同一个数字
        return True
    increase = True if A[i] < A[i + 1] else False
```

得出单调性后，只需要遍历一次数组，判断是否满足单调条件就可以得出结论

时间复杂度O(N) 空间复杂度O(1)