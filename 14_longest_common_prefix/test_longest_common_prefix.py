from unittest import TestCase
from longest_common_prefix import Solution


class TestSolution(TestCase):
    def test_longest_common_prefix(self):
        inputs = (
            ["flower", "flow", "flight"],
            ["dog", "racecar", "car"],
            ["", "b"]
        )
        outs = (
            'fl', '', ""
        )
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().longestCommonPrefix(inp))
