class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        s1, s2 = len(haystack), len(needle)
        p1 = 0
        while p1 < s1 - s2 + 1:
            while p1 < s1 - s2 + 1 and haystack[p1] != needle[0]:
                p1 += 1
            i = 0
            while i < s2 and p1 + i < s1 and haystack[p1 + i] == needle[i]:
                i += 1
            if i == s2:
                return p1
            else:
                p1 += 1
        return -1
