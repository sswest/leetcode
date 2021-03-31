from unittest import TestCase
from search_a_2d_matrix import Solution


class TestSolution(TestCase):
    def test_search_matrix(self):
        inputs = (
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 31)
        )
        outs = (True, False, False)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().searchMatrix(*inp))
