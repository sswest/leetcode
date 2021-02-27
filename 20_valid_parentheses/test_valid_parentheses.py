from unittest import TestCase
from valid_parentheses import Solution


class TestSolution(TestCase):
    def test_is_valid(self):
        inputs = ("()", "()[]{}", "(]", "{[]}")
        outs = (True, True, False, True)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().isValid(inp))
