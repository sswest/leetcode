class Solution:
    def myAtoi(self, s: str) -> int:
        flag, result = 0, 0
        for c in s:
            if flag == 0:
                if c == ' ' or c == 0:
                    continue
                elif c == '-':
                    flag = -1
                    continue
                elif c == '+':
                    flag = 1
                    continue
                elif 47 < ord(c) < 58:
                    flag = 1
                else:
                    break
            else:
                if not (47 < ord(c) < 58):
                    break
            if flag == 1 and (result > 214748364 or (result == 214748364 and ord(c) - 48 > 7)):
                return 2 ** 31 - 1
            if flag == -1 and (result > 214748364 or (result == 214748364 and ord(c) - 48 > 8)):
                return -2 ** 31

            result = result * 10 + ord(c) - 48
        return result * flag



