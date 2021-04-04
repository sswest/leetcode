from unittest import TestCase
from rabbits_in_forest import Solution


class TestSolution(TestCase):
    def test_num_rabbits(self):
        inputs = (
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 5, 10, 10, 10, 7, 10, 10, 10, 10, 10, 10, 10],
            [1, 1, 2],
            [10, 10, 10],
            [],
            [1, 0, 1, 0, 0]
        )
        outs = (36, 5, 11, 0, 5)
        for inp, out in zip(inputs, outs):
            self.assertEqual(Solution().numRabbits(inp), out)
