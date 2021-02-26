## 解题思路

最直观的想法是先遍历每一个puzzle和word，计算包含字母的集合，然后对每一个puzzle遍历words，判断word集合是否为puzzle子集。

这一套思路可行，但时间复杂度太高，会超出时间。可以用位运算+字典来减少时间复杂度。

英文字母最多26位，一个32位整形就可以表示全部英文字母的集合

因此可以将任何一个单词包含的字母用一个整形表示，如

    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    z y x w v u t s r q p o n m l k j i h g f e d c b a
单词able和bale可以用同一个位表示为:

    0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 1 1
    z y x w v u t s r q p o n m l k j i h g f e d c b a

要计算一个字母位运算的方法可以采用将1左移n位，n是该字母离a的位差

1的二进制位source为

    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
        
加入计算字母d的二进制位，则先计算d与a的位差=3，那么字母d的二进制位target=source << 3
        
        0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0

最后将整个单词的字母串起来，使用|位或每一个字母的二进制位，得到整个单词的二进制位`mask`

完全包含同一种字母的单词的mask是相同的，我们可以建立`mask - count`的字典。

建立好字典后，计算`puzzle`单词子集的`sub_mask`，通过字典可以在O(1)时间内获得`sub_mask`的次数。

要计算`puzzle`的子集，可以用将子集的 `sub_mask` 初始为 `puzzle_mask`，然后每次 `sub_mask` 减 1，并和 `puzzle_ask` 进行与操作

下面展示了一个计算过程
```python
sub_mask = puzzle_mask = 1011  # [d, b, a]
(sub_mask - 1) & puzzle_mask = (1011 - 1) & 1011 = 1010 & 1011 = 1010  # [d, b]
(sub_mask - 1) & puzzle_mask = (1010 - 1) & 1011 = 1001 & 1011 = 1001  # [d, a]
(sub_mask - 1) & puzzle_mask = (1001 - 1) & 1011 = 1000 & 1011 = 1000  # [d]
(sub_mask - 1) & puzzle_mask = (1000 - 1) & 1011 = 0111 & 1011 = 0011  # [b, a]
(sub_mask - 1) & puzzle_mask = (0011 - 1) & 1011 = 0010 & 1011 = 0010  # [b]
(sub_mask - 1) & puzzle_mask = (0010 - 1) & 1011 = 0001 & 1011 = 0001  # [a]
(sub_mask - 1) & puzzle_mask = (0001 - 1) & 1011 = 0000 & 1011 = 0000  # []
```

循环`sub_mask = mask & (sub_mask - 1)`过程，直至`sub_mask = 0`结束遍历，就能获得puzzle字符串的全部字符串子集

另一个条件puzzle首字母要存在单词中，可以计算puzzle[0]的mask，与`sub_mask`做位与运算，如果结果为0，表示该子集不包含首字母，应停止计算该子集。