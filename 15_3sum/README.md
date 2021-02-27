## 解题思路

### 方法1
暴力破解法，通过三层循环找到符合条件的答案。时间复杂度至少O(N<sup>3</sup>)，而且答案不能重复，那么还有额外的去重操作。

### 方法2
在方法1的基础下优化，既然题目要求不重复，那么我们只要确保枚举的三个变量`first`,`second`,`third`都和上一次枚举值不同

```python
for first in range(len(nums)):
    if first > 0 and nums[first] == nums[first - 1]:
        continue
    ...
    for second in range(first + 1, len(nums)):
        if second > first + 1 and nums[second] == nums[second - 1]:
            continue
        ...
```

其次，三层枚举也可以使用双指针优化成两层，将`second = len(nums) - 1`，然后向左移动`second`

最终时间复杂度O(N<sup>2</sup>)