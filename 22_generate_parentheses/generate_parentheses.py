from typing import *


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(left: int, right: int):
            if len(compose) == 2 * n:
                result.append(''.join(compose))
            else:
                if left < n:
                    compose.append('(')
                    backtrack(left + 1, right)
                    compose.pop()
                if right < left:
                    compose.append(')')
                    backtrack(left, right + 1)
                    compose.pop()

        compose = []
        backtrack(0, 0)
        return result


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))