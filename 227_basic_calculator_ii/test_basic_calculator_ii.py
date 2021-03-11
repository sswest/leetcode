from unittest import TestCase
from basic_calculator_ii import Solution


class TestSolution(TestCase):
    def test_calculate(self):
        inputs = ("3+2*2", " 3/2 ", " 3+5 / 2 ")
        outs = (7, 1, 5)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().calculate(inp))
