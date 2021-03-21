from unittest import TestCase
from set_matrix_zeroes import Solution


class TestSolution(TestCase):
    def test_set_zeroes(self):
        inputs = (
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        )
        outs = (
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        )
        for inp, out in zip(inputs, outs):
            Solution().setZeroes(inp)
            self.assertEqual(out, inp)
