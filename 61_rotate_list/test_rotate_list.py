from unittest import TestCase
from rotate_list import *


class TestSolution(TestCase):
    def test_rotate_right(self):
        inputs = (
            (list_to_node([1, 2, 3, 4, 5]), 2),
            (list_to_node([0, 1, 2]), 4),
            (list_to_node([1, 2, 3]), 2000000)
        )
        outs = ([4, 5, 1, 2, 3], [2, 0, 1], [2, 3, 1])
        for inp, out in zip(inputs, outs):
            self.assertEqual(node_to_list(Solution().rotateRight(*inp)), out)
