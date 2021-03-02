from unittest import TestCase
from remove_element import Solution


class TestSolution(TestCase):
    def test_remove_element(self):
        inputs = (
            ([3, 2, 2, 3], 3),
            ([0, 1, 2, 2, 3, 0, 4, 2], 2)
        )
        outs = (2, 5)
        for inp, out in zip(inputs, outs):
            self.assertEqual(Solution().removeElement(*inp), out)
