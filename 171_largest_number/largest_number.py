from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        class Compare:
            """对对象进行一层可比较封装 Python3也可以使用functools.cmp_to_key实现相同功能"""
            def __init__(self, obj: str):
                self.obj = obj

            def __lt__(self, other):
                return (self.obj + other.obj) < (other.obj + self.obj)

            def __gt__(self, other):
                return (self.obj + other.obj) > (other.obj + self.obj)

            def __eq__(self, other):
                return (self.obj + other.obj) == (other.obj + self.obj)

            def __le__(self, other):
                return (self.obj + other.obj) <= (other.obj + self.obj)

            def __ge__(self, other):
                return (self.obj + other.obj) >= (other.obj + self.obj)

        nums = sorted(map(str, nums), key=lambda x: Compare(x), reverse=True)
        return "0" if nums[0] == "0" else "".join(nums)
