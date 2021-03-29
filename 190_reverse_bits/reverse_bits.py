class Solution:
    def reverseBits(self, n: int) -> int:
        ans = bin(n)[2:]
        ans = (32 - len(ans)) * '0' + ans
        return int(ans[::-1], 2)
