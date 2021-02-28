from typing import *


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1:
            return True

        i = 0
        while i < len(A) - 2 and A[i] == A[i + 1]:
            i += 1
        if i == len(A) - 1:
            return True

        increase = True if A[i] < A[i + 1] else False

        for i in range(len(A) - 1):
            if increase and A[i + 1] < A[i]:
                return False

            if not increase and A[i + 1] > A[i]:
                return False
        return True
