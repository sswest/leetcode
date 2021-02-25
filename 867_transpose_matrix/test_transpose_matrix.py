from unittest import TestCase
from transpose_matrix import Solution


class TestSolution(TestCase):
    def test_transpose(self):
        inputs = (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[1, 2, 3], [4, 5, 6]]
        )
        outs = (
            [[1, 4, 7], [2, 5, 8], [3, 6, 9]],
            [[1, 4], [2, 5], [3, 6]]
        )
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().transpose(inp))
