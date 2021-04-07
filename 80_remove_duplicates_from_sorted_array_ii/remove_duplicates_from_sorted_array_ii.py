from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        def remind_k(arr: List[int], k: int) -> int:
            """只保留数组中的连续相同的k个元素"""
            if len(arr) < k + 1:
                return len(arr)
            slow = fast = k
            while fast < len(arr):
                if arr[slow - k] != arr[fast]:
                    arr[slow] = arr[fast]
                    slow += 1
                fast += 1
            return slow

        return remind_k(nums, 2)
