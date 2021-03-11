from unittest import TestCase
from make_the_string_great import Solution


class TestSolution(TestCase):
    def test_make_good(self):
        inputs = ('leEeetcode', 'abBAcC', 's')
        outs = ('leetcode', '', 's')
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().makeGood(inp))
