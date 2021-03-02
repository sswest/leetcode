from typing import *


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = []
        for r in range(len(matrix)):
            self.matrix.append([0])
            for c in range(len(matrix[r])):
                self.matrix[r].append(matrix[r][c] + self.matrix[r][-1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2 + 1):
            res += self.matrix[r][col2 + 1] - self.matrix[r][col1]
        return res
