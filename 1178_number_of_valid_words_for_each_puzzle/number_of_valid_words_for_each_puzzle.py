from typing import *

class Solution:
    def get_mask(self, word):
        """英文字母最多26位，一个32位整形就可以表示全部英文字母的集合
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

        最后将整个单词的字母串起来，使用|位或每一个字母的二进制位即可
        """
        mask = 0
        for c in word:
            mask |= 1 << (ord(c) - ord('a'))
        return mask

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        word_hash = dict()
        for word in words:
            mask = self.get_mask(word)  # 计算单词二进制位
            word_hash[mask] = word_hash.get(mask, 0) + 1

        result = []
        for puzzle in puzzles:
            mask = self.get_mask(puzzle)
            head_mask = self.get_mask(puzzle[0])
            sub_mask = mask  # puzzle的子集

            count = 0
            while sub_mask:  # 不断迭代puzzle子集
                if head_mask & sub_mask:  # 用位与运算符&计算头字母是否包含在子集内
                    count += word_hash.get(sub_mask, 0)
                sub_mask = mask & (sub_mask - 1)  # 计算二进制子集
            result.append(count)

        return result


if __name__ == '__main__':
    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = ["actresz"]
    print(Solution().findNumOfValidWords(words, puzzles))