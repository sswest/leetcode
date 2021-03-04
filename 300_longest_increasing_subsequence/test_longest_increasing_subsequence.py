from unittest import TestCase
from longest_increasing_subsequence import Solution


class TestSolution(TestCase):
    def test_length_of_lis(self):
        inputs = (
            [10, 9, 2, 5, 3, 7, 101, 18],
            [0, 1, 0, 3, 2, 3]
        )
        outs = (4, 4)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().lengthOfLIS(inp))
