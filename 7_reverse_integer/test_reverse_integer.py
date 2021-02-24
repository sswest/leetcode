from unittest import TestCase
from reverse_integer import Solution


class TestSolution(TestCase):
    def test_reverse(self):
        _input = -32487249
        out = -94278423
        self.assertEqual(out, Solution().reverse(_input))
