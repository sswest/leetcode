class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # 至少有K个重复字符的最长子串
        # 可以按原字符串中少宇K个的字符分割成子字符串，
        # 继续对子字符串分割处理（递归）
        # 递归结束条件，字符串中所有字符出现次数都大于等于K
        for sp_char in set(s):
            if s.count(sp_char) < k:
                sub_strs = s.split(sp_char)
                return max(*[self.longestSubstring(sub_str, k) for sub_str in sub_strs])
        return len(s)
