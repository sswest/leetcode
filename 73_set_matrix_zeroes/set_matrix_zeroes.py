from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = []
        for r in range(len(matrix)):
            zero = False
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    col.append(c)
                    zero = True
            if zero:
                matrix[r] = [0] * len(matrix[r])
        for r in range(len(matrix)):
            for c in col:
                matrix[r][c] = 0
