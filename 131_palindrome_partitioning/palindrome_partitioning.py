from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        ret, ans = [], []

        def backtrace(i: int):
            if i == n:
                ret.append(ans[:])
            else:
                for j in range(i, n):
                    if f[i][j]:
                        ans.append(s[i:j + 1])
                        backtrace(j + 1)
                        ans.pop()

        backtrace(0)
        return ret
