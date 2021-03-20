from unittest import TestCase
from evaluate_reverse_polish_notation import Solution


class TestSolution(TestCase):
    def test_eval_rpn(self):
        inputs = (
            ["2", "1", "+", "3", "*"],
            ["4", "13", "5", "/", "+"],
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
        outs = (9, 6, 22)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().evalRPN(inp))
