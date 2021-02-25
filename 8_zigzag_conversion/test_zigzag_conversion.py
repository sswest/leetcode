from unittest import TestCase
from zigzag_conversion import Solution


class TestSolution(TestCase):
    def test_convert(self):
        inputs = (
            ('PAYPALISHIRING', 3),
            ('PAYPALISHIRING', 4),
            ('A', 1)
        )
        outs = (
            'PAHNAPLSIIGYIR',
            'PINALSIGYAHRPI',
            'A'
        )
        for inp, out in zip(inputs, outs):
            self.assertEqual(Solution().convert(*inp), out)
