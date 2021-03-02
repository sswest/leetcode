from unittest import TestCase
from remove_duplicates_from_sorted_array import Solution


class TestSolution(TestCase):
    def test_remove_duplicates(self):
        inputs = (
            [1, 1, 2],
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        )
        outs = (2, 5)
        for inp, out in zip(inputs, outs):
            self.assertEqual(Solution().removeDuplicates(inp), out)
