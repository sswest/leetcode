from unittest import TestCase
from find_minimum_in_rotated_sorted_array import Solution


class TestSolution(TestCase):
    def test_find_min(self):
        inputs = (
            [3, 4, 5, 1, 2],
            [4, 5, 6, 7, 0, 1, 2],
            [11, 13, 15, 17]
        )
        outs = (1, 0, 11)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().findMin(inp))
