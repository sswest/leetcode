from unittest import TestCase
from letter_combinations_of_a_phone_number import Solution


class TestSolution(TestCase):
    def test_letter_combinations(self):
        inputs = ('23', '', '2')
        outs = (
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
            [],
            ["a", "b", "c"]
        )
        for inp, out in zip(inputs, outs):
            print(Solution().letterCombinations(inp))
