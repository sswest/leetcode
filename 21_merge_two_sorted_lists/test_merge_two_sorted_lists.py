from unittest import TestCase
from merge_two_sorted_lists import *


class TestSolution(TestCase):
    def test_merge_two_lists(self):
        inputs = (
            ([1, 2, 4], [1, 3, 4]),
            ([], []),
            ([], [0])
        )
        outs = ([1, 1, 2, 3, 4, 4], [], [0])
        for inp, out in zip(inputs, outs):
            ret = Solution().mergeTwoLists(list_to_node(inp[0]), list_to_node(inp[1]))
            self.assertEqual(node_to_list(ret), (out))
