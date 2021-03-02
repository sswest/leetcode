from unittest import TestCase
from range_sum_query_2d_immutable import NumMatrix


class TestNumMatrix(TestCase):
    def test_sum_region(self):
        matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
        ]
        obj = NumMatrix(matrix)
        inputs = (
            (2, 1, 4, 3),
            (1, 1, 2, 2),
            (1, 2, 2, 4)
        )
        outs = (8, 11, 12)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, obj.sumRegion(*inp))
