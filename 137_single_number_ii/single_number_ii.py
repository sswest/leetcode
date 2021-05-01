from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        return min(count.keys(), key=lambda x: count[x])
