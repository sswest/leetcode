from unittest import TestCase
from next_greater_element_i import Solution


class TestSolution(TestCase):
    def test_next_greater_element(self):
        inputs = (
            ([4, 1, 2], [1, 3, 4, 2]),
            ([2, 4], [1, 2, 3, 4])
        )
        outs = ([-1, 3, -1], [3, -1])
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().nextGreaterElement(*inp))
