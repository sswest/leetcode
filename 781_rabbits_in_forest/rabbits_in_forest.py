import math
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        table = dict()
        for n in answers:
            table[n] = table.get(n, 0) + 1
        ans = 0
        for k, v in table.items():
            if v <= k + 1:
                ans += k + 1
            else:
                ans += math.ceil(v / (k + 1)) * (k + 1)
        return ans
