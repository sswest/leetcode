from unittest import TestCase
from number_of_1_bits import Solution


class TestSolution(TestCase):
    def test_hamming_weight(self):
        inputs = (
            int(b'00000000000000000000000000001011', 2),
            int(b'00000000000000000000000010000000', 2),
            int(b'11111111111111111111111111111101', 2),
        )
        outs = (3, 1, 31)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().hammingWeight(inp))
