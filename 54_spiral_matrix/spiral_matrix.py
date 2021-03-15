from typing import *


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        ans = [0] * (n * m)

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        r, c = 0, 0
        direction_index = 0

        for i in range(m * n):
            ans[i] = matrix[r][c]
            visited[r][c] = True
            next_row = r + directions[direction_index][0]
            next_col = c + directions[direction_index][1]
            if not (0 <= next_row < m and 0 <= next_col < n and not visited[next_row][next_col]):
                direction_index = (direction_index + 1) % 4
            r += directions[direction_index][0]
            c += directions[direction_index][1]
        return ans

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        ans = []

        def outside(left: int, right: int, top: int, bottom: int):
            if len(ans) == len(matrix) * len(matrix[0]):
                return
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                ans.append(matrix[i][right])
            if top != bottom:
                for i in range(right - 1, left - 1, -1):
                    ans.append(matrix[bottom][i])
            if left != right:
                for i in range(bottom - 1, top, - 1):
                    ans.append(matrix[i][left])
            if left < right:
                left += 1
            if right > left:
                right -= 1
            if top < bottom:
                top += 1
            if bottom > top:
                bottom -= 1
            outside(left, right, top, bottom)

        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        outside(left, right, top, bottom)
        return ans
