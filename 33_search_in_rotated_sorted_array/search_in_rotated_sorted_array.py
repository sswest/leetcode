from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                k = i
                break
        nums = nums[k:] + nums[:k]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid + k
                if result > len(nums) - 1:
                    result %= len(nums)
                return result
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
