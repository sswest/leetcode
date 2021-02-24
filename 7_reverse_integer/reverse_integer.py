class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        flag = 1 if x >= 0 else - 1
        x = abs(x)
        while x > 0 or x % 10:
            result = result * 10 + x % 10
            x //= 10
        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 0
        return flag * result


