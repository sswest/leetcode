from unittest import TestCase
from spiral_matrix import Solution


class TestSolution(TestCase):
    def test_outside(self):
        inputs = (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[6, 9, 7]]
        )
        outs = (
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
            [6, 9, 7]
        )
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().spiralOrder(inp))