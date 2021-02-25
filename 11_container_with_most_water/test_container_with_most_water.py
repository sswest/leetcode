from unittest import TestCase
from container_with_most_water import Solution


class TestSolution(TestCase):
    def test_max_area(self):
        inputs = (
            [1, 8, 6, 2, 5, 4, 8, 3, 7],
            [1, 1],
            [4, 3, 2, 1, 4],
            [1, 2, 1]
        )
        outs = (49, 1, 16, 2)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().maxArea(inp))
