from unittest import TestCase
from string_to_integer_atoi import Solution


class TestSolution(TestCase):
    def test_my_atoi(self):
        inp = '   -004193 2with words'
        out = -4193
        self.assertEqual(out, Solution().myAtoi(inp))
