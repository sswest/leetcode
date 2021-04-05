from unittest import TestCase
from merge_sorted_array import Solution


class TestSolution(TestCase):
    def test_merge(self):
        inputs = (
            ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
            ([1], 1, [], 0)
        )
        outs = ([1, 2, 2, 3, 5, 6], [1])
        for inp, out in zip(inputs, outs):
            Solution().merge(*inp)
            self.assertEqual(inp[0], out)
