from unittest import TestCase
from next_greater_element_ii import Solution


class TestSolution(TestCase):
    def test_next_greater_elements(self):
        inputs = (
            [1, 2, 1, 3, 5, 2],
            [1, 2, 1]
        )
        outs = (
            [2, 3, 3, 5, -1, 3],
            [2, -1, 2]
        )
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().nextGreaterElements(inp))
