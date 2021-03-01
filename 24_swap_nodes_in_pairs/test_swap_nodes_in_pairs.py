from unittest import TestCase
from swap_nodes_in_pairs import *


class TestSolution(TestCase):
    def test_swap_pairs(self):
        inputs = ([1, 2, 3, 4], [], [1])
        outs = ([2, 1, 4, 3], [], [1])
        for inp, out in zip(inputs, outs):
            inp = list_to_node(inp)
            ret = node_to_list(Solution().swapPairs(inp))
            self.assertEqual(out, ret)
