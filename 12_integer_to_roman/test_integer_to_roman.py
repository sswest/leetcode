from unittest import TestCase
from integer_to_roman import Solution


class TestSolution(TestCase):
    def test_int_to_roman(self):
        outs = ('III', 'IV', 'IX', 'LVIII', 'MCMXCIV')
        inputs = (3, 4, 9, 58, 1994)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().intToRoman(inp))
