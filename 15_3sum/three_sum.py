from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for first in range(len(nums)):
            third = len(nums) - 1
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, len(nums)):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[first] + nums[second] + nums[third] > 0:
                    third -= 1
                if second == third:
                    break
                if nums[first] + nums[second] + nums[third] == 0:
                    result.append([nums[first], nums[second], nums[third]])
        return result
