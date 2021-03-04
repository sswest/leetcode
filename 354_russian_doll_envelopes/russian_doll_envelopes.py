from typing import *


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        enve = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        f = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if enve[j][1] < enve[i][1]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f)
