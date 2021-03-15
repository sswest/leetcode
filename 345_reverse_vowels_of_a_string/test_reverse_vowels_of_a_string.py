from unittest import TestCase
from reverse_vowels_of_a_string import Solution


class TestSolution(TestCase):
    def test_reverse_vowels(self):
        inputs = (
            "leetcode",
            'Aa',
            "hello"
        )
        outs = ("leotcede", 'aA', 'holle')
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, Solution().reverseVowels(inp))
