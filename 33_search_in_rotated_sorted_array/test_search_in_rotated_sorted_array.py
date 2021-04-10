from unittest import TestCase
from search_in_rotated_sorted_array import Solution


class TestSolution(TestCase):
    def test_search(self):
        inputs = (
            ([3, 1], 3),
            ([4, 5, 6, 7, 0, 1, 2], 0),
            ([4, 5, 6, 7, 0, 1, 2], 3),
            ([1], 0)
        )
        outs = (0, 4, -1, -1)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().search(*inp))
