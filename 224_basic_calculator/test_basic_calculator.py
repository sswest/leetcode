from unittest import TestCase
from basic_calculator import Solution


class TestSolution(TestCase):
    def test_calculate(self):
        inputs = ("1 + 1", "(1+(4+5+2)-3)+(6+8)", "(1+(4+5+2)-3)+(6+82)")
        outs = (2, 23, 97)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().calculate(inp))
