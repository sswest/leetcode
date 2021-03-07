from unittest import TestCase
from palindrome_partitioning import Solution


class TestSolution(TestCase):
    def test_partition(self):
        inputs = ('aab',)
        outs = (
            [["aa", "b"], ["a", "a", "b"]],
        )
        for inp, out in zip(inputs, outs):
            ret = Solution().partition(inp)
            out.sort()
            ret.sort()
            self.assertEqual(ret, out)
