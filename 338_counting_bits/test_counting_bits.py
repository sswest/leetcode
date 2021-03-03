from unittest import TestCase
from counting_bits import Solution


class TestSolution(TestCase):
    def test_count_bits(self):
        inputs = (2, 5, 10)
        outs = (
            [0, 1, 1],
            [0, 1, 1, 2, 1, 2],
            [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
        )
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().countBits(inp))
