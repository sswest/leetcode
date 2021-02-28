from unittest import TestCase
from monotonic_array import Solution


class TestSolution(TestCase):
    def test_is_monotonic(self):
        inputs = (
            [1, 2, 2, 3],
            [6, 5, 4, 4],
            [1, 3, 2],
            [1, 2, 4, 5],
            [1, 1, 1]
        )
        outs = (True, True, False, True, True)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().isMonotonic(inp))
