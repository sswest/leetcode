## 解题思路

### 暴力法

最直观的解法使用三层遍历，得出所有组合，如果都不满足条件返回False

时间复杂度O(n<sup>3</sup>) 该方法会超出时间限制

### 两层遍历优化

注意到题目总是左边的数字最小，因此题目可以分解为在第一个数字小于第二个数字的情况下，满足第二个数字大于第三个数字且第三个数字大于第一个数字

而第一个数字只需要取左边的最小值就行，可以随着第二个数字的遍历在O(1)的时间内得出，这样就减少了一层遍历，时间复杂度为O(n<sup>2</sup>)