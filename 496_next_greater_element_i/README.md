## 解题思路

单调栈 + 哈希表

单调栈中存储下标，哈希表存储 元素： 下一个更大的数

每次从`nums2`中取出一个数`num`，不断栈顶中的索引`i`对应的数`nums[i]`比较。

如果`num`更大，则`num[i]`的下一个更大元素就是`num`，此时将栈顶出栈，写入哈希表`dict[num[i]] = num`，然后将`num`的索引压入栈。

如果`num`小于或等于`num[i]`，那么直接将`num`的索引入栈。

    