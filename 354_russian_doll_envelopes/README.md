## 解题思路

### 动态规划

先对二维数组中的其中一维按升序排序，问题就转化成求一维数组的[最大上升子序列](https://github.com/sswest/leetcode/tree/master/300_longest_increasing_subsequence)

特别要关注h[i] <= h[i+1]时，无法组成套娃信封，而之前对一维数组求最大上升子序列的解法是严格考虑顺序的，因此在使用动态规划算法前可以对第二维数据降序来排除h[i] = h[i+1]的影响。