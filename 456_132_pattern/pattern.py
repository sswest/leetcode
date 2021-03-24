from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        i = 0
        for j in range(1, len(nums) - 1):
            if nums[j] > nums[i]:
                # i 和 j已经找到 找k
                for k in range(j + 1, len(nums)):
                    if nums[j] > nums[k] and nums[k] > nums[i]:
                        return True
            else:
                i = j  # 第一个数取最小值
        return False
