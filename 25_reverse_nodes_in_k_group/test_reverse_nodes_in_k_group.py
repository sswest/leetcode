from unittest import TestCase
from reverse_nodes_in_k_group import *


class TestSolution(TestCase):
    def test_reverse_kgroup(self):
        inputs = ([[1, 2, 3, 4, 5], 3], [[1, 2, 3, 4, 5], 1], [[1], 1])
        outs = ([3, 2, 1, 4, 5], [1, 2, 3, 4, 5], [1])
        for inp, out in zip(inputs, outs):
            inp[0] = list_to_node(inp[0])
            ret = node_to_list(Solution().reverseKGroup(*inp))
            self.assertEqual(out, ret)
