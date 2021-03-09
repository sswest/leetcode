from unittest import TestCase
from search_insert_position import Solution


class TestSolution(TestCase):
    def test_search_insert(self):
        inputs = (
            ([1, 3, 5, 6], 5),
            ([1, 3, 5, 6], 2),
            ([1, 3, 5, 6], 7),
        )
        outs = (2, 1, 4, 0)
        for inp, out in zip(inputs, outs):
            self.assertEqual(Solution().searchInsert(*inp), out)
