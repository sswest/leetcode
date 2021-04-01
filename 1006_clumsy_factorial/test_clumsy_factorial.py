from unittest import TestCase
from clumsy_factorial import Solution


class TestSolution(TestCase):
    def test_clumsy(self):
        inputs = (10, 9, 73, 4)
        outs = (12, 11, 75, 7)
        for inp, out in zip(inputs, outs):
            self.assertEqual(Solution().clumsy(inp), out)
