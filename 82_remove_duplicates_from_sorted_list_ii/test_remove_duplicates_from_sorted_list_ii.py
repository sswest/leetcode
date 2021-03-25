from unittest import TestCase
from remove_duplicates_from_sorted_list_ii import *


class TestSolution(TestCase):
    def test_delete_duplicates(self):
        inputs = (
            list_to_node([1, 2, 3, 3, 4, 4, 5]),
            list_to_node([1, 1, 1, 2, 3]),
        )
        outs = (
            [1, 2, 5],
            [2, 3]
        )
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, node_to_list(Solution().deleteDuplicates(inp)))
