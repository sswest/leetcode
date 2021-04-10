from unittest import TestCase
from ugly_number import Solution


class TestSolution(TestCase):
    def test_is_ugly(self):
        inputs = (6, 8, 14, 30, 1, -5)
        outs = (True, True, False, True, False, False)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().isUgly(out))
