from unittest import TestCase
from four_sum import Solution


class TestSolution(TestCase):
    def test_four_sum(self):
        inputs = (
            ([1, 0, -1, 0, -2, 2], 0),
        )
        outs = ([[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]],)
        for inp, out in zip(inputs, outs):
            ret = Solution().fourSum(*inp)
            ret.sort()
            out.sort()
            self.assertEqual(out, ret)
