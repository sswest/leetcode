from typing import *


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 构建字典树
        tree, length = dict(), None
        for s in strs:
            length = len(s) if length is None else min(length, len(s))
            node = tree
            for char in s:
                node[char] = node.get(char, dict())
                node = node[char]
        result, node = '', tree
        while True:
            if len(result) == length:
                break
            if len(node) == 1:  # 该节点只有一个key-value对 表示所有单词拥有同一个字母
                key = list(node.keys())[0]
                result += key
                node = node[key]
            else:
                break
        return result


if __name__ == '__main__':
    Solution().longestCommonPrefix(["flower", "flow", "flight"])
