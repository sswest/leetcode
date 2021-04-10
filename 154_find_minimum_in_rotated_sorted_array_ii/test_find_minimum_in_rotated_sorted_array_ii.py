from unittest import TestCase
from find_minimum_in_rotated_sorted_array_ii import Solution


class TestSolution(TestCase):
    def test_find_min(self):
        inputs = (
            [2, 2, 2, 2, 1],
            [1, 3, 5],
            [2, 2, 2, 0, 1]
        )
        outs = (1, 1, 0)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().findMin(inp))
