from typing import *

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            left, right = 0, len(A[i]) - 1
            while left < right:
                A[i][left], A[i][right] = A[i][right] ^ 1, A[i][left] ^ 1
                left += 1
                right -= 1
            if left == right:
                A[i][left] ^= 1
        return A
