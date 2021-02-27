from typing import *


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:3])
        close = abs(result - target)
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, len(nums)):
                third = len(nums) - 1
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while third > second:
                    r = nums[first] + nums[second] + nums[third]
                    c = abs(r - target)
                    if c < close:
                        result = r
                        close = c
                    third -= 1
        return result

