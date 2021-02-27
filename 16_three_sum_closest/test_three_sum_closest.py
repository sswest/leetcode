from unittest import TestCase
from three_sum_closest import Solution


class TestSolution(TestCase):
    def test_three_sum_closest(self):
        inputs = (
            ([-1, 2, 1, -4], 1),
        )
        outs = (2,)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().threeSumClosest(*inp))
