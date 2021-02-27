from typing import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phones = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                  '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if not digits:
            return []

        def backtrace(_index: int) -> None:
            """回溯算法
            :param _index: 当前已加入的字符串位置
            :return:
            """
            if _index == len(digits):
                # 递归结束条件
                combinations.append(''.join(combination))
            else:
                for char in phones[digits[_index]]:
                    combination.append(char)
                    backtrace(_index + 1)
                    combination.pop()

        combination, combinations = [], []
        backtrace(0)
        return combinations
