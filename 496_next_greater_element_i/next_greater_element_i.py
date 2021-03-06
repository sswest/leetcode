from typing import *


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        table = {}
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                table[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        ans = []
        for i in nums1:
            ans.append(table.get(i, -1))
        return ans
