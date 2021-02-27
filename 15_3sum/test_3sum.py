from unittest import TestCase
from three_sum import Solution


class TestSolution(TestCase):
    def test_three_sum(self):
        inputs = (
            [-1, 0, 1, 2, -1, -4],
            [],
            [0]
        )
        outs = ([[-1, -1, 2], [-1, 0, 1]], [], [])
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().threeSum(inp))

