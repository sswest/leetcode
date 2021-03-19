from unittest import TestCase
from reverse_linked_list_ii import *


class TestSolution(TestCase):
    def test_reverse_between(self):
        ln1 = list_to_node([1, 2, 3, 4, 5])
        ln2 = list_to_node([3, 5])

        inputs = ((ln1, 2, 4), (ln2, 1, 1))
        outs = ([1, 4, 3, 2, 5], [3, 5])
        for inp, out in zip(inputs, outs):
            result = Solution().reverseBetween(*inp)
            self.assertEqual(out, node_to_list(result))
