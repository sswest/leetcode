from typing import *


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        ret = [[0 for i in range(r)] for j in range(c)]
        for row in range(r):
            for col in range(c):
                ret[col][row] = matrix[row][col]
        return ret
