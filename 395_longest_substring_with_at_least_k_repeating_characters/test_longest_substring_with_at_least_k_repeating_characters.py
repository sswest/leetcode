from unittest import TestCase
from longest_substring_with_at_least_k_repeating_characters import Solution


class TestSolution(TestCase):
    def test_longest_substring(self):
        inputs = (
            ('aaabb', 3),
            ('ababbc', 2),
            ('aaabbb', 3),
        )
        outs = (3, 5, 6)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().longestSubstring(*inp))
