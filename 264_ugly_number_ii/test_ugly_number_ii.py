from unittest import TestCase
from ugly_number_ii import Solution


class TestSolution(TestCase):
    def test_nth_ugly_number(self):
        inputs = (10, 1)
        outs = (12, 1)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().nthUglyNumber(inp))
