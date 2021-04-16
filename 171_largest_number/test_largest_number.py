from unittest import TestCase
from largest_number import Solution


class TestSolution(TestCase):
    def test_largest_number(self):
        inputs = (
            (10, 2),
            (3, 30, 34, 5, 9),
            (1,),
            (10,)
        )
        outs = ('210', '9534330', '1', '10')
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().largestNumber(inp))
