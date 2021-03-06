## 解题思路

### 回溯法

先使用哈希表存储数字和字符的对应关系，回溯过程类似二叉树的中序遍历。

回溯过程中维护一个初始为空的字符串，表示已有的字母排列。每次取电话号码的一位数字，从哈希表中获得该数字对应的所有可能的字母，并将其中的一个字母插入到已有的字母排列后面，然后继续处理电话号码的后一位数字，直到处理完电话号码中的所有数字，即得到一个完整的字母排列。然后进行回退操作，遍历其余的字母排列。

回溯算法用于寻找所有的可行解，如果发现一个解不可行，则会舍弃不可行的解。在这道题中，由于每个数字对应的每个字母都可能进入字母组合，因此不存在不可行的解，直接穷举所有的解即可。

时间复杂度O(3<sup>m</sup>+4<sup>n</sup>)  空间复杂度O(m+n)
