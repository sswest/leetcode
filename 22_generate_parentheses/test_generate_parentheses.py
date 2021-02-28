from unittest import TestCase
from generate_parentheses import Solution


class TestSolution(TestCase):
    def test_backtrack(self):
        inputs = (3, 1)
        outs = (
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
            ["()"]
        )
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().generateParenthesis(inp))
