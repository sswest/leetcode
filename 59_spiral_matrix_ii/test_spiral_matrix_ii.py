from unittest import TestCase
from spiral_matrix_ii import Solution


class TestSolution(TestCase):
    def test_generate_matrix(self):
        inputs = (
            3, 1
        )
        outs = (
            [[1, 2, 3], [8, 9, 4], [7, 6, 5]],
            [[1]]
        )
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().generateMatrix(inp))
