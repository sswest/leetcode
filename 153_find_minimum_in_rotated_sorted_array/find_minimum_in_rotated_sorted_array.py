from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                n = i
                break
        return nums[n]
