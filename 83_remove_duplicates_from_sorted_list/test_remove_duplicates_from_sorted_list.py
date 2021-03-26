from unittest import TestCase
from remove_duplicates_from_sorted_list import *


class TestSolution(TestCase):
    def test_delete_duplicates(self):
        inputs = (
            list_to_node([1, 1, 2, 3, 3]),
            list_to_node([0, 0, 0, 0]),
            list_to_node([1, 1, 2]),
        )
        outs = ([1, 2, 3], [0], [1, 2])
        for inp, out in zip(inputs, outs):
            self.assertEqual(node_to_list(Solution().deleteDuplicates(inp)), out)
