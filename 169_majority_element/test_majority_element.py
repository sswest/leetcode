from unittest import TestCase
from majority_element import Solution


class TestSolution(TestCase):
    def test_majority_element(self):
        inputs = (
            [3, 2, 3],
            [2, 2, 1, 1, 1, 2, 2]
        )
        outs = (3, 2)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().majorityElement(inp))
