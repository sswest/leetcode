# @Date    : 2021-04-10
# @Author  : song wei
# @email   : songwei@clickwifi.net
from unittest import TestCase
from search_in_rotated_sorted_array_ii import Solution


class TestSolution(TestCase):
    def test_search(self):
        inputs = (
            ([2, 5, 6, 0, 0, 1, 2], 0),
            ([2, 5, 6, 0, 0, 1, 2], 3)
        )
        outs = (True, False)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().search(*inp))
