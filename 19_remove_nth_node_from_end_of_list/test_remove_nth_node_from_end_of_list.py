from unittest import TestCase
from remove_nth_node_from_end_of_list import *


class TestSolution(TestCase):
    def test_remove_nth_from_end(self):
        inputs = (
            ([1, 2], 2),
            ([1, 2], 1),
            ([1, 2, 3, 4, 5], 2)
        )
        outs = ([2], [1], [1, 2, 3, 5])
        for inp, out in zip(inputs, outs):
            ret = Solution().removeNthFromEnd(list_to_node(inp[0]), inp[1])
            self.assertEqual(node_to_list(ret), (out))
