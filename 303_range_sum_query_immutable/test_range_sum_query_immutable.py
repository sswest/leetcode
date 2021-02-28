from unittest import TestCase
from range_sum_query_immutable import *


class TestNumArray(TestCase):
    def test_sum_range(self):
        inputs = [[0, 2], [2, 5], [0, 5]]
        outs = [1, -1, -3]
        obj = NumArray([-2, 0, 3, -5, 2, -1])
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, obj.sumRange(*inp))
