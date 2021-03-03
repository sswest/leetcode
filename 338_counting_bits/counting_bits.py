from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        # 方法一
        result = []
        for i in range(num + 1):
            x, count = i, 0
            while x > 0:
                x &= (x - 1)
                count += 1
            result.append(count)
        return result
