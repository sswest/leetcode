from unittest import TestCase
from single_number_ii import Solution


class TestSolution(TestCase):
    def test_single_number(self):
        inputs = (
            [2, 2, 3, 2],
            [0, 1, 0, 1, 0, 1, 99]
        )
        outs = (3, 99)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().singleNumber(inp))
