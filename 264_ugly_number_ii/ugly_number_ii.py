import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap, cur = [1], 1
        rp = set()
        while cur < n:
            _min = heapq.heappop(heap)
            for i in (2, 3, 5):
                if i * _min not in rp:
                    rp.add(i * _min)
                    heapq.heappush(heap, i * _min)
            cur += 1
        return heapq.heappop(heap)
