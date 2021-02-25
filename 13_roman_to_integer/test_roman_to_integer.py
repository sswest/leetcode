from unittest import TestCase
from roman_to_integer import Solution


class TestSolution(TestCase):
    def test_roman_to_int(self):
        inputs = ('III', 'IV', 'IX', 'LVIII', 'MCMXCIV')
        outs = (3, 4, 9, 58, 1994)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().romanToInt(inp))
