
class Solution:
    def isPalindrome(self, x: int) -> bool:
        _x, y = x, 0
        if x < 0:
            return False
        while x:
            mantissa = x % 10
            x //= 10
            y = y * 10 + mantissa
        return _x == y
