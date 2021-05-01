from unittest import TestCase
from sum_of_square_numbers import Solution


class TestSolution(TestCase):
    def test_judge_square_sum(self):
        inputs = (5, 3, 4, 2, 1)
        outs = (True, False, True, True, True)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().judgeSquareSum(inp))
