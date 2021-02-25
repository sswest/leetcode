class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ret = ['' for i in range(numRows)]
        r, flag = 0, -1
        for char in s:
            ret[r] += char
            if r == 0 or r == numRows - 1:
                flag = -flag
            r += flag
        return ''.join(ret)
