from unittest import TestCase
from remove_duplicates_from_sorted_array_ii import Solution


class TestSolution(TestCase):
    def test_remind_k(self):
        inputs = (
            [1, 1, 1, 2, 2, 3],
            [0, 0, 1, 1, 1, 1, 2, 3, 3]
        )
        outs = (
            [1, 1, 2, 2, 3],
            [0, 0, 1, 1, 2, 3, 3]
        )
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, inp[:Solution().removeDuplicates(inp)])
