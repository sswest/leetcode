## 解题思路

如果不考虑特殊情况，一个字符永远能够对应一个数字，那么只要遍历字符串每一个字符，用`哈希表`找到对应的数字加起来即可。

实际情况是存在多个字符组合的特殊情况，那么在遍历字符串的时候可以判断后续的2个字符是否能组成一个数字。

时间复杂度O(n) 空间复杂度O(1)