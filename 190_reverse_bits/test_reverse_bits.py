from unittest import TestCase
from reverse_bits import Solution


class TestSolution(TestCase):
    def test_reverse_bits(self):
        inputs = (
            int(b'00000010100101000001111010011100', 2),
            int(b'11111111111111111111111111111101', 2),
            int(b'00000010100101000001111010011100', 2),
            int(b'11111111111111111111111111111101', 2)
        )
        outs = (
            int(b'00111001011110000010100101000000', 2),
            int(b'10111111111111111111111111111111', 2),
            int(b'00111001011110000010100101000000', 2),
            int(b'10111111111111111111111111111111', 2)
        )
        for inp, out in zip(inputs, outs):
            self.assertEqual(Solution().reverseBits(inp), out)
